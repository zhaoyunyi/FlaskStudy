# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import Response

app = Flask(__name__)


@app.route('/getjsonstr', methods=['GET'])
def get_json():
    data = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
    return jsonify(result=data)


if __name__ == '__main__':
    app.run(debug=True)