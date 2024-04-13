from flask import Flask, render_template, make_response, jsonify, url_for, redirect
from forms.text import SendTextForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I LOVE PYTHON LETS GOOOOO'


def main():
    app.run(port=5000, host='127.0.0.1')


@app.route("/")
def base():
    return render_template("main.html", title="Главная")


@app.route("/send_text", methods=['get', 'post'])
def send_text():
    form = SendTextForm()
    if form.validate_on_submit():
        text = form.text.data
        picture = form.picture.data
        picture.save('static/img/img.png')

        return redirect('/')

    return render_template("send_text.html", title="Выслать текст", form=form)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    main()
