from django.views.generic.base import TemplateView

from . import DjangoBlockRenderer


def render_template(request, template_name, block_list, context=None):
    return DjangoBlockRenderer(
        request, template_name, block_list, context=context
    ).render()


class BlockRenderView(TemplateView):
    """Class view to enable partial rendering."""
    default_blocks = {}
    blocks = {}

    def get_block_list(self):
        block_list = self.default_blocks.copy()
        block_list.update(self.blocks)
        return block_list

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return DjangoBlockRenderer(
            request, self.template_name, self.get_block_list(), context
        ).render()
