import jwt
from datetime import datetime, timedelta
from flaskrest import app
from flask import request, jsonify
from flaskrest.api.auth.models import User


def create_token(user):
    token = jwt.encode({'id': user.id, 'exp': datetime.utcnow(
    ) + timedelta(minutes=30)}, app.config['SECRET_KEY'])
    return token.decode('UTF-8')


def check_token(f):
    def wrapper(*args, **kwargs):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'ok': False, 'error': 'Login Required'}), 401
        try:
            token_data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(id=token_data['id']).first()
        except jwt.InvalidTokenError:
            return jsonify({'ok': False, 'error': 'Invalid Token'}), 401
        return f(current_user, *args, **kwargs)
    return wrapper
