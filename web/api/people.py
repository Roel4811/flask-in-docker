# -*- coding: utf-8 -*-
"""
The people API
"""
import flask
from flask import jsonify

blueprint = flask.Blueprint('people', __name__, url_prefix='/api/people')

static_people = [
    {
        'id': 1,
        'first_name': 'Peter',
        'last_name': 'Zand',
        'email': 'petervtzand@gmail.com'
    },
    {
        'id': 2,
        'first_name': 'Barack',
        'last_name': 'Obama',
        'email': 'mail_barack@gmail.com'
    },
    {
        'id': 3,
        'first_name': 'Donald',
        'last_name': 'Duck',
        'email': 'donald_duck@gmail.com'
    }
]

@blueprint.route('/<int:person_id>')
def person_item(person_id):
    """Return a person, based on id

    example url: `api/people/1

    example json:
    {
        'person': {
            'id': 1,
            'first_name': 'Peter',
            'last_name': 'Zand',
            'email': 'petervtzand@gmail.com'
        }
    }

    """
    for person in static_people:
        if person['id'] == person_id:
            return jsonify(person)
        else:
            return jsonify(no_person_found())

@blueprint.route('/')
def people_list():
    """
    Return people

    Filters:
    - first_name (like filter) e.g. first_name=a, matches `Donald` & `Barack`, since it contains an a
    - last_name (like_filter)
    - email (equals filter)


    Sort_by (descending and ascending)
    - first_name
    - last_name
    - email
    - id

    Pagination
    - Results per page (default=2)
    - Page number (default = 0)

    example url: `api/people/?last_name=a&sort_by=first_name&results_per_page=1&page_number=0

    example json:
    {
        'people': [
            {
                'id': 1,
                'first_name': 'Barack',
                'last_name': 'Obama',
                'email': 'mail_barack@gmail.com'
            }
        ],
        'meta_data': {
            'total_results': 2,
            'total_pages': 2,
            'page_number': 0
            'sort_by': 'first_name',
            'filters': ['last_name']
        }
    }

    """
    return 'TODO return json of people + metadata, with request args: %s' % str(dict(flask.request.args))

def no_person_found():
    return {
        'code': 404,
        'message': "Person not found"
    }
