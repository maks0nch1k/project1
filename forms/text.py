from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired
from sqlalchemy_serializer import SerializerMixin


class SendTextForm(FlaskForm, SerializerMixin):
    text = TextAreaField("Your text:", validators=[DataRequired()])
    picture = FileField("Изображение", validators=[FileAllowed(['jpg', 'png'],
                                                               'Загрузить можно только файлы jpg, png')])
    submit = SubmitField("Check")