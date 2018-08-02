# -*- coding: utf-8 -*-

from flask import Flask
from flask import abort, redirect, url_for
from flask import render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    # 注意不要带 '/' 在前面
    return redirect(url_for('login'))


@app.route('/login')
def login():
    # 给 WSGI 程序抛出一个异常
    print('进到了 重定向页面')
    # 可以直接在return respone 之前抛出一个http 协议的状态码
    abort(401)
    abort(404)
    return '进到了 重定向页面'


# 默认情况下，错误代码会显示一个黑白的错误页面。如果你要定制错误页面， 可以使用
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


'''如果返回的是一个合法的响应对象，它会从视图直接返回。
如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 (response, status, headers) 的形式，且至少包含一个元素。 status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。 '''


@app.errorhandler(401)
def page_not_enter(error):
    response = make_response('401 禁止访问', 401)
    response.headers['X-Something'] = '啊'.encode("utf-8") # 需要中文编码把 bytes 变成str
    return response


if __name__ == '__main__':
    app.run(debug=True)
