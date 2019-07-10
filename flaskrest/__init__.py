from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['FLASK_REST_DB_URL']
app.config['SECRET_KEY'] = os.environ['FLASK_REST_SECRET']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)

from flaskrest.api import api_blueprint

app.register_blueprint(api_blueprint)


from flaskrest.api.auth import models
