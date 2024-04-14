from flask_restful import Resource
from flask import jsonify


class TextResource(Resource):
    def get(self, filename):
        with open(f'static/txt/{filename}.txt') as file:
            text = file.read()
        text += 'mbeee'
        return jsonify({'fixed': {'accept_pic': False,
                                  'text': text}})