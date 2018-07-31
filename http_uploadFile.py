# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def uplaod_file():
    if request.method == 'POST':
        file = request.files.get('the_file') # 上传文件带key 并且from-data 方式
        print(file)

        if file is not None:
            file.save('/Users/zhaoyunyi/uploaded_file.jpeg')
            print('不安全的用户名' + file.filename)
        else:
            return '上传文件失败，没有读到对应文件 key the_file'
        # WSGI 工具包 封装一类有用底层的工具类对象
        return '上传文件成功 文件名为 ' + secure_filename(file.filename)

    if request.method == 'GET':
        return 'get upload'


if __name__ == '__main__':
    app.run(debug=True)