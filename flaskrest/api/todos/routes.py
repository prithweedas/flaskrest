from flask import jsonify

from flaskrest.api import api_blueprint
from flaskrest.api.todos.models import Todo
from flaskrest.api.todos import todo_schema, todos_schema
from flaskrest.api.auth.utils import check_token


@api_blueprint.route('/todo')
@check_token
def get_all_todos(current_user):
    return jsonify({'ok': True, 'todos': todos_schema.dump(
                    Todo.query.filter_by(user_id=current_user.id)).data})
