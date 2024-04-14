from flask_restful import Resource
from flask import jsonify
from toxicity import ToxicCommentsDetector


class TextResource(Resource):
    def get(self, filename):
        with open(f'static/txt/{filename}.txt') as file:
            text = file.read()

        test_raw_texts = text.split()
        mbe = ToxicCommentsDetector()
        print(mbe.predict(test_raw_texts))

        return jsonify({'fixed': {'accept_pic': True,
                                  'text': text}})