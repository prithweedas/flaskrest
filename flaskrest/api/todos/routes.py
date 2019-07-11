from flask import jsonify, request

from flaskrest.api import api_blueprint
from flaskrest.api.todos.models import Todo
from flaskrest.api.todos import todo_schema, todos_schema
from flaskrest.api.auth.utils import check_token
from flaskrest import db


@api_blueprint.route('/todo')
@check_token
def get_all_todos(current_user):
    return jsonify({'ok': True, 'todos': todos_schema.dump(
                    Todo.query.filter_by(user_id=current_user.id)).data})


@api_blueprint.route('/todo/create', methods=['POST'])
@check_token
def create_todo(current_user):
    print(request.json)
    todo = Todo(request.json['title'],
                request.json['description'], current_user)
    db.session.add(todo)
    db.session.commit()
    return jsonify({'ok': True, 'todo': todo_schema.dump(todo).data})
