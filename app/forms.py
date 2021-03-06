#!/usr/bin/env python

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, URL, Length

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class URLForm(Form):
    url = StringField('Image URL', validators=[DataRequired(),URL(require_tld=True,message="That is not a valid link url!")])
