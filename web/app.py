# -*- coding: utf-8 -*-
"""
Flask App

"""
from flask import Flask

import flask
import api
import json
from api.people import people_list
from api.tasks import tasks_list
from datetime import datetime


def init_app(app):
    """init some thingies"""
    api.init_app(app)


def create_app():
    app = Flask(__name__)

    init_app(app)
    return app


app = create_app()


@app.route('/')
def index_route():
    """Test"""
    return 'I don\'t belong here!'


@app.route('/people')
def people_route():
    """Nice page to show people"""
    response = people_list()
    data = json.loads(response.get_data())
    people = data['people']
    time = datetime.now().isoformat()
    return flask.render_template('people.html', title = "my people", people = people, time = time)


@app.route('/tasks')
def tasks_route():
    """Nice page to show tasks"""
    response = tasks_list()
    data = json.loads(response.get_data())
    tasks = data['tasks']
    time = datetime.now().isoformat()
    return flask.render_template('tasks.html', title = "my tasks", tasks = tasks, time = time)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
