from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username         = StringField("Foydalanuvchi nomi", validators=[InputRequired(), Length(min=3)])
    email            = StringField("Email", validators=[InputRequired(), Email()])
    password         = PasswordField("Parol", validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField("Parolni tasdiqlang", validators=[EqualTo('password')])
    submit           = SubmitField("Ro‘yxatdan o‘tish")

class LoginForm(FlaskForm):
    email    = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Parol", validators=[InputRequired()])
    submit   = SubmitField("Kirish")

class PostForm(FlaskForm):
    title   = StringField("Sarlavha", validators=[InputRequired()])
    content = TextAreaField("Mazmun", validators=[InputRequired()])
    submit  = SubmitField("Saqlash")
