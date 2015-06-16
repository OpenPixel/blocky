from flask import Flask

from flask_blocky import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('child.html', {'content': '.content'})

if __name__ == '__main__':
    app.run()
