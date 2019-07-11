from flaskrest import ma


class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id,''title', 'date_posted', 'description')
