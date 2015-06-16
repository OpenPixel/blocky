from flask import jsonify, request
from flask.globals import _app_ctx_stack
from flask.templating import _render
from flask.views import MethodView

from jinja2 import nodes


__all__ = [
    'BlockDoesNotExist', 'build_response', 'render_template', 'BaseRenderView'
]


class BlockDoesNotExist(Exception):
    """Used in our renderer to handle when a block is missing"""
    pass


def build_response(tmpl, block_list, block_funcs, context):
    """Build the response dict.

    Example: ::
    """
    response = list()

    for name, selector in block_list.iteritems():
        try:
            response.append({
                'name': name,
                'selector': selector,
                'content': ''.join(block_funcs[name](context))
            })
        except KeyError:
            raise BlockDoesNotExist(
                "Block {0} could not be found.".format(name)
            )

    return {
        'blocks': response,
        'url': request.path,
        'pushState': True,
    }


def _render_blocks(jinja_env, template, template_name, block_list, **context):
    source = jinja_env.loader.get_source(
        jinja_env, template_name)[0]
    parsed = jinja_env.parse(source)

    blocks = dict()
    new_context = None
    extend_node = parsed.find(nodes.Extends)

    if extend_node:
        extend_template = jinja_env.get_or_select_template(
            extend_node.template.value
        )
        blocks = extend_template.blocks
        new_context = extend_template.new_context(context)
    else:
        new_context = template.new_context(context)

    for name, func in template.blocks.iteritems():
        blocks[name] = func

    return jsonify(
        build_response(template, block_list, blocks, new_context)
    )


def render_template(template_name, block_list, **context):
    """Provide a method to render the block or full template.

    This method uses `flask.request.is_xhr <http://flask.pocoo.org
    /docs/0.10/api/#flask.Request.is_xhr>`_ to determine the request type.

    Args:
        template_name: A string matching the template path.
        block_list: A dictionary of blocks in {blockname: css_selector}
            format
        context: The kwargs to pass into the template as context

    Returns:


    Example: ::
        return render_template(
            'home.html', {'content': '.content'}, {'name': 'Joe'}
        )
    """
    ctx = _app_ctx_stack.top
    ctx.app.update_template_context(context)
    jinja_env = ctx.app.jinja_env
    context.update({
        'content_template': template_name
    })

    template = jinja_env.get_or_select_template(template_name)

    if request.is_xhr:
        return _render_blocks(
            jinja_env, template, template_name, block_list, **context
        )
    else:
        return _render(template, context, ctx.app)


class BaseRenderView(MethodView):
    """Class view to enable partial rendering."""
    template_name = None  # The template for the view
    default_blocks = {}
    blocks = {}

    def render_template(self, **context):
        block_list = self.default_blocks.copy()
        block_list.update(self.blocks)

        return render_template(self.template_name, block_list, **context)
