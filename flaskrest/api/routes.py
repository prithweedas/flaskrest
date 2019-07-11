import flaskrest.api.auth.routes
import flaskrest.api.todos.routes
import csv
from flaskrest.api import api_blueprint
from flaskrest import basedir
import os
from flask import jsonify


@api_blueprint.route('/rain')
def get_rain_data():
    csvfile = os.path.join(basedir, '..', 'raindata.csv')
    data = []
    with open(csvfile, 'r') as file:
        reader = list(csv.reader(file))
        for row in reader[1:]:
            data.append({'district': row[0], 'rain': {
                '2011': row[2],
                '2012': row[4],
                '2013': row[6],
                '2014': row[8]
            }})
    return jsonify({'ok': True, 'data': data})
