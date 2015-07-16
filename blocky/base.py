from jinja2 import nodes


__all__ = ['BlockDoesNotExist', 'BlockRenderer']


class BlockDoesNotExist(Exception):
    """Used in our renderer to handle when a block is missing"""
    pass


class BlockRenderer(object):
    def __init__(self):
        raise NotImplementedError

    def is_xhr(self):
        raise NotImplementedError

    def get_template(self, template_name):
        raise NotImplementedError

    def get_path(self):
        return self.request.path

    def build_json(self, block_funcs):
        response = list()

        for name, selector in self.blocks.iteritems():
            try:
                response.append({
                    'name': name,
                    'selector': selector,
                    'content': ''.join(block_funcs[name](self.context))
                })
            except KeyError:
                raise BlockDoesNotExist(
                    "Block {0} could not be found.".format(name)
                )

        return {
            'blocks': response,
            'url': self.get_path()
        }

    def build_response(self, block_funcs):
        raise NotImplementedError

    def get_template_blocks(self, template):
        raise NotImplementedError

    def new_context(self, template):
        raise NotImplementedError

    def render_blocks(self):
        source = self.jinja_env.loader.get_source(
            self.jinja_env, self.template_name
        )[0]
        parsed = self.jinja_env.parse(source)

        blocks = dict()
        new_context = None
        extend_node = parsed.find(nodes.Extends)

        if extend_node:
            extend_template = self.get_template(extend_node.template.value)
            blocks = self.get_template_blocks(extend_template)
            new_context = self.new_context(extend_template)
        else:
            new_context = self.new_context(self.template)

        for name, func in self.get_template_blocks(
            self.template).iteritems():
            blocks[name] = func

        return self.build_response(blocks)

    def render_template(self):
        raise NotImplementedError

    def render(self):
        if self.is_xhr():
            return self.render_blocks()
        else:
            return self.render_template()
