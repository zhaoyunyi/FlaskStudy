# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import json


app = Flask(__name__)


@app.route('/getjsonify', methods=['GET'])
def get_json():
    data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    return jsonify(result=data)
# jsonify 可以传入对象为参数，并且支持多参对象转json，在head 里的返回 content-type →application/json
# 会在body 里返回对应的json 对象


@app.route('/getdumps', methods=['GET'])
def getdumps():
    data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    return json.dumps(data)
# python 自带的dumps 输出的是html/text 文本，并不是json类型的数据，并且不支持多参
# content-type →text/html; charset=utf-8


if __name__ == '__main__':
    app.run(debug=True)