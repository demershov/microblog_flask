from app import app
from flask import render_template


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
    return render_template('index.html', title='Микроблог', user=user)
