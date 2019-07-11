from flaskrest import ma
from marshmallow import fields
from flaskrest.api.auth.schema import UserSchema


class TodoSchema(ma.Schema):
    owner = fields.Nested(UserSchema)

    class Meta:
        fields = ('id', 'title', 'date_posted', 'description', 'owner')
