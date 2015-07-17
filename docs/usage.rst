Usage
=====

Blocky can be used in both Flask and Django. For both frameworks, you can use a method call or a class view.

When passing in the blocks to render, we always use a dictionary with the following format: ::

    {
        block_name: css_selector
    }

Flask
-----

Direct Method
^^^^^^^^^^^^^

::

    from blocky.flask.shortcuts import render_template

    @app.route('/')
    def home():
        return render_template('home.html', {'content': '.content'}, form=form)

Class View
^^^^^^^^^^

::

    from blocky.flask.shortcuts import BlockRenderView

    class AppBaseView(BlockRenderView):
        default_blocks = {
            'title': 'title',
            'messages': '.messages',
        }

    class HomeView(AppBaseView):
        template_name = 'home.html'
        blocks = {
            'content': '.content'
        }

        def get(self):
            return self.render_template(form=form)

    app.add_url_rule('/', view_func=HomeView.as_view('home'))

Although there is slightly more setup initially, it allows for more configuration and less repition when defining common blocks. The above example shows a way in which you can use default_blocks. This is already part of our base class view and allows for inheritance of class views. In the above example, home will respond with three blocks ('title', 'messages' and 'content').

Django
------

Direct Method
^^^^^^^^^^^^^

::

    from blocky.django.shortcuts import render_template

    def home(request):
        return render_template(request, 'child.html', {'content': '.content'}, {'form': form})

Class View
^^^^^^^^^^

::

    from blocky.django.shortcuts import BlockRenderView

    class HomeView(BlockRenderView):
        template_name = 'home.html'
        default_blocks = {
            'title': 'title',
            'messages': '.messages',
        }
        blocks = {
            'content': '.content'
        }
