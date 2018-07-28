# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)  # 默认导入main


@app.route('/')  # route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    # app.debug = True  # 开始debug模式让程序修改后能直接重新更新服务
    # app.run()  # app.run(host='0.0.0.0') 让操作系统监听所有公网 IP
    app.run(debug=True)
