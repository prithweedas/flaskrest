from flaskrest import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, description, user):
        self.title = title
        self.description = description
        self.user_id = user.id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
