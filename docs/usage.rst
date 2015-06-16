Usage
=====

There are two ways to use flask_blocky. Either call our rendering method directly, or to make use of a Class based view for added customization.

Direct Method
-------------

Here is an example using our direct method ::

    from flask_blocky import render_template

    @app.route('/')
    def home():
        return render_template('home.html', {'content': '.content'})

We pass in the template name and a dictionary of blocks to render. The dictionary is in the following format ::

    {
        block_name: css_selector
    }

Class View
----------

Here is an example using our class view ::

    from flask_blocky import BaseRenderView

    class AppBaseView(BaseRenderView):
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
            return self.render_template({'name': 'Jim'})

    app.add_url_rule('/', view_func=HomeView.as_view('home'))

Although there is slightly more setup initially, it allows for more configuration. The above example shows a way in which you can use default_blocks. This is already part of our base class view and allows for inheritance of class views. In the above example, home will respond with three blocks ('title', 'messages' and 'content').
