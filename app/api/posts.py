from app import app, db
from flask import jsonify, request, url_for
from app.models import Post, User
from .errors import bad_request
from .auth import token_auth


@app.route('/api/posts/', methods=['GET'])
@token_auth.login_required
def get_posts():
    page = request.args.get('offset', 1, type=int)
    per_page = min(request.args.get('count', 1, type=int), 100)
    data = Post.to_collection_dict(Post.query.order_by(Post.date.desc()), page, per_page, 'get_posts')
    return jsonify(data)


@app.route('/api/posts/<int:id>', methods=['GET'])
@token_auth.login_required
def get_post(id):
    return jsonify(Post.query.get_or_404(id).to_dict())


@app.route('/api/posts/', methods=['POST'])
@token_auth.login_required
def create_post():
    data = request.get_json() or {}
    token = request.headers['Authorization'].split(' ')[-1]

    if 'title' not in data or 'body' not in data:
        return bad_request('Запрос должен включать такие ключи как: title, body')
    elif len(data['title']) > 255 or len(data['title']) < 10:
        return bad_request('Длина заголовка не может быть меньше 10 или больше 255')
    elif len(data['body']) > 4000 or len(data['body']) < 1:
        return bad_request('Длина тела поста не может быть меньше 1 или больше 4000')

    user = User.query.filter_by(token=token).first()

    if not user:
        return bad_request('Такого пользователя нет')

    data['user_id'] = user.id
    post = Post()
    post.from_dict(data)
    db.session.add(post)
    db.session.commit()
    response = jsonify(post.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_post', id=post.id)
    print(response)
    return response