# -*- coding: utf-8 -*-
from flask import Flask
from datetime import datetime
from marshmallow import Schema, pprint, fields, post_load

app = Flask(__name__)


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self.created_at = datetime.now()


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)


user = User(name="Jean Zhao", email="zcloudswing@gmail.com")
schema = UserSchema()
result = schema.dump(user)
pprint(result.data)

user_data = {
    # 'created_at': '2018-08-13T22:58:02.531094+00:00',
    'email': 'zcloudswing@gmail.com',
    'name': 'zhaoyunyi'
}

schema = UserSchema()
result = schema.load(user_data)

pprint(result.data)
pprint(result.data.__dict__)

'''
{'created_at': '2018-08-13T22:57:18.659984+00:00',
 'email': 'zcloudswing@gmail.com',
 'name': 'Jean Zhao'}
'''

if __name__ == 'main':
    app.run(debug=True)