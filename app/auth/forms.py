from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username = StringField("enter your name: ", validators=[DataRequired(), Length(min=5)])
    password = PasswordField("enter your password: ", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("ok")

class SignUpForm(FlaskForm):
    username = StringField("enter your name: ", validators=[DataRequired(), Length(min=5)])
    email = StringField("enter your email", validators=[DataRequired(), Email()])
    password = PasswordField("enter your password: ", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("ok")