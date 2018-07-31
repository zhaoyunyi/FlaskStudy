# -*- coding: utf-8 -*-

from flask import Flask, request, make_response
from flask import  render_template

app = Flask(__name__)


@app.route('/getcookies')
def get_cookies():
    username = request.cookies.get('username')
    if username is not None:
        return 'cookies 中的username 为' + username

    return 'cookies 中的 没有username 数据'


@app.route('/setcookies')
def set_cookies():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('username', 'the username Jean')
    return resp

if __name__ == '__main__':
    app.run(debug=True)