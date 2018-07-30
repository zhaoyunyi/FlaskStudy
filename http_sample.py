# -*- coding: utf-8 -*-

from flask import Flask, request
from werkzeug.datastructures import ImmutableMultiDict

# from flask import make_response,Response

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'GET':
        # args 只获取 get 提交过来数据 request.values 能获取全部
        get_username = request.args.get('name')
        return 'get 方法获取的username 参数 %s' % get_username + '全部的参数字典值 %s' % request.values

    # post 协议方法需要注意处理 http - head的情况，有异常的情况最后清空
    if request.method == 'POST':
        # request_form 只获取 post 提交的表单 form-data 数据
        postData = request.form
        # request.values 可以同时获取到 get 相关数据
        get_username = request.values.get('name')

        # print(request.form.get('username', type=str, default=None))
        # print(request.values.get('name', default='little apple'))
        # datax = request.form.to_dict()

        logStr = 'post 提交的 form-data 数据 %s' % postData \
                 + '\n全部的参数字典值 %s' % request.values \
                 + '\n同时取到get方法带来的参数 %s' % request.args

        print(logStr)
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhaoyunyi' and password == '123':
            return '恭喜您 ' + username + '登录成功'
        else:
            error = '用户名或者密码不正确'

    return error


if __name__ == '__main__':
    app.run(debug=True)
