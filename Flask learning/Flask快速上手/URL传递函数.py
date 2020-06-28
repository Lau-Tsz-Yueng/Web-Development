# encoding:utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '这是url传参演示！'


@app.route('/news/<int:id>')
def list_news(id):
    return 'zhangsan'


@app.route('/user/<str:name>')
def listQ(name):
    return (name)


if __name__ == '__main__':
    app.run(debug=True)
