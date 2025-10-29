from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import session
import random


class LoginForm(FlaskForm):
    username = StringField("enter your name: ", validators=[DataRequired(), Length(min=5)])
    password = PasswordField("enter your password: ", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("ok")

class SignUpForm(FlaskForm):
    username = StringField("enter your name: ", validators=[DataRequired(), Length(min=5)])
    email = StringField("enter your email", validators=[DataRequired(), Email()])
    password = PasswordField("enter your password: ", validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField("تکرار رمز", validators=[DataRequired(), EqualTo("password")])

    
    captcha = StringField("کپچا", validators=[DataRequired()])
    submit = SubmitField("ok")


class UploadProfilePictureForm(FlaskForm):
    profile_picture = FileField('عکس پروفایل', validators=[DataRequired()])
    submit = SubmitField('آپلود')