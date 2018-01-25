from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Григорий'}
    posts = [
        {
            'author': 'Михаил',
            'body': 'Мой первый блог на Фласке'
        },
        {
            'author': 'Дмитрий',
            'body': 'Раз, два, три, кто не спрятался, я не виноват'
        },
        {
            'author': 'Александр',
            'body': 'Кто тум самый храбрый?'
        }
    ]
    return render_template('index.html', title='Микроблог', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)
