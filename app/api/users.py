from app import app
from flask import jsonify, request
from app.models import User


@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@app.route('/api/users/', methods=['GET'])
def get_users():
    page = request.args.get('offset', 1, type=int)
    per_page = min(request.args.get('count', 1, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'get_users')
    return jsonify(data)


@app.route('/users', methods=['POST'])
def create_user():
    pass


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass