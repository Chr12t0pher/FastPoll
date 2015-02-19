from wtforms import StringField, RadioField, SelectField, TextAreaField
from flask_wtf import Form
from .models import Poll
from app import db


class CreatePoll(Form):
    title = StringField("Title")
    options = TextAreaField("Options")
