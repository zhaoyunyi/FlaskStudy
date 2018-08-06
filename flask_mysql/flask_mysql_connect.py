from flask import Flask
from flask_sqlalchemy import SQLAlchemy

'''配置数据库'''
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

# 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名jianshu,连接方式参考 \
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://zhaoyunyi:zhaoyunyi@127.0.0.1:3306/zz1207'
#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
#实例化
db = SQLAlchemy(app)