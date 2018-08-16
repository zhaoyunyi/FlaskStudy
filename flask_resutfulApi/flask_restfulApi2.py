# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask.json import JSONEncoder

app = Flask(__name__)
api = Api(app)


# 自定义一个基础返回数据类
class MyBaseResponse(object):

    def __init__(self):
        self.data = None
        self.code = 0
        self.msg = '服务器异常'

    def serialize(self):
        return {
            'data': self.data,
            'code': self.code,
            'msg': self.msg,
        }


# 自定义Json 解析模板
class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MyBaseResponse):
            return {
                'data': obj.data,
                'code': obj.code,
                'msg': obj.msg,
            }
        return super(MyJSONEncoder, self).default(obj)

# 配置给flask json_encoder
app.json_encoder = MyJSONEncoder

# 通过put修改一个静态变量，模拟数据库修改
user = {'user_id': '11',
        'username': 'GiGi',
        'age': 18}


userList = [{'user_id': '11',
        'username': 'GiGi',
        'age': 18},
         {'user_id': '31',
        'username': 'Jean',
        'age': 30},
         {'user_id': '21',
        'username': 'zhaoyunyi',
        'age': 20}
     ]

myResponse = MyBaseResponse()


class UserName(Resource):
    def get(self, user_id):
        if user.get('user_id') == user_id:
            myResponse.data = user
            myResponse.code = 200
            myResponse.msg = '获取用户成功'
        else:
            myResponse.code = 2001
            myResponse.msg = 'user_id 为 %s 的用户不存在' % user_id
        return jsonify(myResponse)

    def put(self, user_id):
        if user.get('user_id') != user_id:
            myResponse.data = user
            myResponse.code = 2001
            myResponse.msg = 'user_id 为 %s 的用户不存在' % user_id
            return jsonify(myResponse)

        username = request.form.get('username')
        if username is None:
            myResponse.code = 2002
            myResponse.msg = '未提交对应userName 参数'
            return jsonify(myResponse)

        user['username'] = username
        myResponse.data = user
        myResponse.code = 200
        myResponse.msg = '用户名字修改成功'

        return jsonify(myResponse)


class UserList(Resource):
    def get(self):
        myResponse.data = userList
        myResponse.code = 200
        myResponse.msg = '获取用户成功'
        return jsonify(myResponse)


api.add_resource(UserName, '/<string:user_id>')


api.add_resource(UserList, '/userlist')

if __name__ == '__main__':
    app.run(debug=True)
