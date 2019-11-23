# -*- coding: utf-8 -*-

from . import people
from . import tasks

def init_app(app):
    """Init all API blueprints"""
    app.register_blueprint(people.blueprint)
    app.register_blueprint(tasks.blueprint)
