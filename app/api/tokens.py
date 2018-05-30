from flask import jsonify, g
from app import db, app
from .auth import basic_auth


@app.route('/api/tokens/', methods=['POST'])
@basic_auth.login_required
def get_token():
    print('!!!!!!')
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token': token})