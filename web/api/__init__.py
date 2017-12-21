# -*- coding: utf-8 -*-

from . import people


def init_app(app):
    """Init all API blueprints"""
    app.register_blueprint(people.blueprint)
