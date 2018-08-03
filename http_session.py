# -*- coding: utf-8 -*-

from flask import Flask
from flask import session, redirect, url_for, escape, request

app = Flask(__name__)

# session 密钥签名加密的 cookie ，即用户可以查看你的 cookie ，但是如果没有密钥就无法修改它。
# 设置秘钥
app.secret_key = 'Jean_session_secret_key'
# app.config['SECRET_KEY'] = os.urandom(24) 安全的密钥

@app.route('/')
def index():
    if 'username' in session:
        return '正在登录中的用户是 %s' % escape(session.get('username'))
    return '未有用户登录'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # 退出操作
    session.pop('username', None)
    return redirect(url_for('index'))
    # 清除session中所有数据
    # session.clear

if __name__ == '__main__':
    app.run(debug=True)