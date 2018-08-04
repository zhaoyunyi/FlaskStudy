# -*- coding: utf-8 -*-

from flask import Flask, logging

app = Flask(__name__)


@app.route('/logger')
def logger():
    app.logger.debug('输出debug 日志')
    app.logger.warning('输出 warning 警告')
    app.logger.error('输出 错误 信息')
    return '日志输出测试'

if __name__ == '__main__':
    app.run(debug=True)