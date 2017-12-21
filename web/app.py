# -*- coding: utf-8 -*-
"""
Flask App

"""
from flask import Flask

import flask
import api
import json


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
    return flask.render_template('people.html', title='My People')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
