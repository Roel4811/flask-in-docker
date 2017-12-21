# -*- coding: utf-8 -*-
"""
Flask App

"""
from flask import Flask

import api


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
