from flaskrest.api.todos.schema import TodoSchema

todo_schema = TodoSchema(strict=True)
todos_schema = TodoSchema(many=True, strict=True)
