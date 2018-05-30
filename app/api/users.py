from app import app, db
from flask import jsonify, request, url_for
from app.models import User
from .errors import bad_request
from .auth import token_auth


@app.route('/api/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@app.route('/api/users/', methods=['GET'])
@token_auth.login_required
def get_users():
    page = request.args.get('offset', 1, type=int)
    per_page = min(request.args.get('count', 1, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'get_users')
    return jsonify(data)


@app.route('/api/users/', methods=['POST'])
def create_user():
    print('!!!', request.get_json())
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('Запрос должен вклчать такие ключи как: username, email, password')
    elif User.query.filter_by(username=data['username']).first():
        return bad_request('Пожалуйста, используйте другой username, т.к этот занят.')
    elif User.query.filter_by(email=data['email']).first():
        return bad_request('Пожалуйста, используйте другой email, т.к этот занят.')

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('get_user', id=user.id)
    return response


@app.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json() or {}

    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return bad_request('Пожалуйста, используйте другой username, т.к этот занят.')

    if 'email' in data and data['email'] != user.email and User.query.filter_by(email=data['email']).first():
        return bad_request('Пожалуйста, используйте другой email, т.к этот занят.')

    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())