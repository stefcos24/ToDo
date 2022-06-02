from ast import Sub
from calendar import day_abbr
import imp
from tokenize import String
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from flask_login import current_user
from todoproject.models import User


class LoginForm(FlaskForm):

    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):

    email = StringField('Email: ', validators=[DataRequired(), Email()])
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('password_confirm', message='Password must match!')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This email is already taken!')
    
    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is already taken!')


class UpdateUserForm(FlaskForm):

