from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import ValidationError
from flask_wtf import Form
from flask import flash


class CreatePoll(Form):
    title = StringField("Title")
    desc = StringField("Description")
    options = TextAreaField("Options")
    public = BooleanField("Public")

    def validate_options(self, field):
        options = []
        for option in field.data.split("\n"):
            options.append(option.strip("\r"))
        if len(options) != len(set(options)):
            flash("You have duplicate options.", "danger")
            raise ValidationError("Duplicate Options")
        if len(options) <= 1:
            flash("Please have at least 2 options.", "info")
            raise ValidationError("Not Enough Options")
        if len(options) > 10:
            flash("Please have no more than 10 options.", "info")
            raise ValidationError("Too Many Options")