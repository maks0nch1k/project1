from flask import Flask, render_template, make_response, jsonify, redirect, session
from flask_restful import Api
from forms.text import SendTextForm
import data.text_resource as text_resource
from requests import get
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'I LOVE PYTHON LETS GOOOOO'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=1)
api = Api(app)
api.add_resource(text_resource.TextResource, '/api/text/<string:filename>')


def main():
    app.run(port=5000, host='127.0.0.1')


@app.route("/")
def base():
    return render_template("main_page.html", title="Главная")


@app.route("/send_text", methods=['get', 'post'])
def send_text():
    form = SendTextForm()
    if form.validate_on_submit():
        text = form.text.data
        picture = form.picture.data
        session['filename'] = str(datetime.datetime.now()).replace('.', '-').replace(' ', '-')
        with open(f"static/txt/{session['filename']}.txt", "w") as file:
            file.write(text)
        if picture is not None:
            picture.save(f'static/img/{session["filename"]}.png')
            session['is_pic'] = True
        else:
            session['is_pic'] = False

        return redirect('/fixed_text')

    return render_template("send_text.html", title="Выслать текст", form=form)


@app.route("/fixed_text")
def fixed_text():
    ans = get(f'http://127.0.0.1:5000/api/text/{session["filename"]}').json()
    return render_template("fixed_text.html", title="Исправленный текст",
                           text=ans['fixed']['text'], accept_img=ans['fixed']['accept_pic'],
                           is_pic=session['is_pic'], filename=session['filename'])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    main()
