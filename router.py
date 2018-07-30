# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '这是主页'


@app.route('/detail')
def detail():
    return '这是详情页'


# 可以在路径里面添加转换规则
@app.route('/user/<username>')
def user(username):
    return '用户名字为 %s' % username


# 同一个user路径下优先匹配类型合适的 如果都是同一个类型则按定义顺序的前后进行匹配
@app.route('/user/<int:uid>')
def show_user(uid):
    return '用户编号为 %s' % uid


# 如果最后的路径名 带上了 斜杠'/' 则会匹配为 路径path
@app.route('/user/<path:path_name>')
def show_path(path_name):
    return '执行路径为 %s ' % path_name


# 接收读点类型路径数据 匹配到 . 号就会进入改路由 多个 . 不影响
@app.route('/user/<float:weight>')
def show_user_weight(weight):
    return '用户体重是 %s ' % weight


# 唯一 URL / 重定向行为 如果带 / 测绘 404
@app.route('/about')
def about():
    return '这是关于页面'


# 不加 / 会重定向到带 / 的情况
@app.route('/help/')
def show_help():
    return '这是帮助页面'


if __name__ == '__main__':
    app.run(debug=True)
