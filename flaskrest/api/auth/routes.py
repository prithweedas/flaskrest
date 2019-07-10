from flask import request, jsonify

from flaskrest.api import api_blueprint
from flaskrest.api.auth import user_schema, users_schema
from flaskrest.api.auth.models import User
from flaskrest import db, bcrypt
from flaskrest.api.auth.utils import create_token, check_token

'''
Every route in this file will start with '/auth'
'''


@api_blueprint.route('/auth/register', methods=['POST'])
def create_user():
    hashed_password = bcrypt.generate_password_hash(request.json['password'])
    new_user = User(request.json['email'], hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'ok': True, 'user': user_schema.dump(new_user).data})


@api_blueprint.route('/auth/login', methods=['POST'])
def login():
    user = User.query.filter_by(email=request.json['email']).first()

    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_token(user)
        return jsonify({'ok': True, 'user': user_schema.dump(user).data, 'token': token})

    return jsonify({'ok': False, 'error': 'Wrong email or password'})


@api_blueprint.route('/auth/users', methods=['GET'])
@check_token
def get_users(current_user):
    users = User.query.all()
    return users_schema.jsonify(users)
