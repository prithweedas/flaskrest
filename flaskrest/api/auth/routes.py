from flask import jsonify

from flaskrest.api import api_blueprint


@api_blueprint.route('/auth/')
def index():
    return jsonify({'ok': True})
