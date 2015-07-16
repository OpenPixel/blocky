from flask.json import jsonify
from flask.globals import _app_ctx_stack, request
from flask.templating import _render

from jinja2 import nodes

from ..base import BlockRenderer


class FlaskBlockRenderer(BlockRenderer):
    def __init__(self, template_name, blocks, **context):
        self.template_name = template_name
        self.blocks = blocks
        self.context = context

        self.app = _app_ctx_stack.top.app
        self.jinja_env = self.app.jinja_env

        self.template = self.get_template(self.template_name)

    def get_path(self):
        return request.path

    def is_xhr(self):
        return request.is_xhr

    def get_template_blocks(self, template):
        return template.blocks

    def new_context(self, template):
        return template.new_context(self.context)

    def get_template(self, template_name):
        return self.jinja_env.get_or_select_template(template_name)

    def build_response(self, block_funcs):
        return jsonify(self.build_json(block_funcs))

    def render_template(self):
        return _render(self.template, self.context, self.app)
