from flask.views import MethodView

from . import FlaskBlockRenderer

__all__ = ['render_template', 'BaseRenderView']

def render_template(template_name, block_list, **context):
    return FlaskBlockRenderer(template_name, block_list, **context).render()


class BlockRenderView(MethodView):
    """Class view to enable partial rendering."""
    template_name = None  # The template for the view
    default_blocks = {}
    blocks = {}

    def render_template(self, **context):
        block_list = self.default_blocks.copy()
        block_list.update(self.blocks)

        return FlaskBlockRenderer(
            self.template_name, block_list, **context
        ).render()
