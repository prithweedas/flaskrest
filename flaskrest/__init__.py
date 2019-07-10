from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['FLASK_BLOG_DB_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

from flaskrest.api import api_blueprint

app.register_blueprint(api_blueprint)
