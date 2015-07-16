import json

from django.shortcuts import render
from django.test import TestCase, RequestFactory

from .views import home


class DjangoBlockyTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_renders_content_block(self):
        request = self.factory.get('/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        response = home(request)
        assert response.status_code == 200

        json_response = json.loads(response.content)
        assert 'blocks' in json_response
        assert filter(
            lambda x: x['name'] == 'content', json_response['blocks']
        )

    def test_render_template(self):
        request = self.factory.get('/')

        response = home(request)
        assert response.status_code == 200

        expected = render(request, 'response.html')

        assert expected.content == response.content
