from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, length
from flask import flash


class ContactForm(FlaskForm):
    name = StringField('Name:')
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    message = TextAreaField('Message:', validators=[DataRequired(), length(max=500)])
    submit = SubmitField('Submit')

class VIPOfferForm(FlaskForm):
    name = StringField('Name:')
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    submit = SubmitField('Click to Join VIP List')
