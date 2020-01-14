from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class weatherform(FlaskForm):
    city = StringField('city')
    submit = SubmitField('submit')
    