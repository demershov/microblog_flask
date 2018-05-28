from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User
from flask import request


class SearchForm(FlaskForm):
    q = StringField(('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('Такого пользователя не существует!')

    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            if not user.check_password(password.data):
                raise ValidationError('Неверно указан пароль!')

    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста, используйте другой логин')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Этот email уже используется')


class EditProfileForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField('Сохранить')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Этот логин уже занят!')

    def validate_email(self, email):
        if email.data != User.query.filter_by(username=self.original_username).first().email:
            user = User.query.filter_by(email=self.email.data).first()
            if user is not None:
                raise ValidationError('Этот email уже используется')

    # def validate_about_me(self, about_me):
    #     if about_me.data:
    #         text = about_me.data
    #         if len(text) > 140 or len(text) <= -1:
    #             raise ValidationError('Этот логин уже занят!')


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(), Length(min=10, max=255)])
    body = TextAreaField('Содержание', validators=[DataRequired(), Length(min=1, max=4000)])
    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')