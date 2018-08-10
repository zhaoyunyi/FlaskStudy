# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# 封装restful定义的视图api，然后添加到Api 对象中绑定路径和资源
class FlaskRestfulApi(Resource):
    def get(self):
        return {'The first Api': 'Hello World'}


api.add_resource(FlaskRestfulApi, '/')

# 通过put修改一个静态变量，模拟数据库修改
userName = {'11': 'GiGi'}


class UserName(Resource):
    def get(self, user_id):
        return {user_id: userName[user_id]}

    def put(self, user_id):
        userName[user_id] = request.form.get('userName')
        return  {user_id: userName[user_id]}

api.add_resource(UserName, '/<string:user_id>')


if __name__ == '__main__':
    app.run(debug=True)
