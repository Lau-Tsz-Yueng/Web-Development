# encoding: utf-8
from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("首先访问了index()这个视图函数了！")
    urll = url_for('user_login')
    return redirect(urll)


@app.route('/user_login')
def user_login():
    return "这是用户登陆界面，请你登陆，才能访问首页！"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='1231')
