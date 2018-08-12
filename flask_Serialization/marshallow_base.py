# -*- coding: utf-8 -*-
from flask import Flask
from datetime import date
from marshmallow import Schema, pprint, fields

app = Flask(__name__)


class ArtistSchema(Schema):
    name = fields.Str()


'''
要对一个类（记为Class_A，以便表达）进行序列化和反序列化，首先要创建一个与之对应的类（记Class_A'），
负责实现Class_A的序列化、序列化和数据校验等，Class_A'就是schema，
'''


class AlbumSchema(Schema):
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema)

bowie = dict(name='zhaoyunyi')
album = dict(artist=bowie, title='GiGi', release_date=date(1971, 12, 17))

schema = AlbumSchema()
result = schema.dump(album)
pprint(result, indent=2)

'''MarshalResult(data={
    'artist': {'name': 'zhaoyunyi'}, 'title': 'GiGi', 'release_date': '1971-12-17'
    }, errors={})
'''
if __name__ == 'main':
    app.run(debug=True)
