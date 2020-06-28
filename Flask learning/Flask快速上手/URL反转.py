# encoding: utf-8
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    urll = (url_for('news', id='10086'))
    return "URL反转内容为: %s" % urll


@app.route('/news/<id>')
def news(id):
    return u'您请求的参数是: %s' % id


if __name__ == '__main__':
    app.run(debug=True)
