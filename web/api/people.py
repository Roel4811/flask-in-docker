# -*- coding: utf-8 -*-
"""
The people API
"""
import flask
from flask import jsonify
from flask import abort
import math

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
            abort(404, {'message': 'Person not found'})

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
    sort_param = flask.request.args.get('sort_by') or 'Not Set'
    page_number = flask.request.args.get('page_number') or 0
    results_per_page = flask.request.args.get('results_per_page') or 2
    people = search_people()

    return jsonify({
        'people': sorted(people, key = lambda person: person[sort_param]),
        'meta_data': {
            'total_results': len(people),
            'total_pages': math.ceil(len(people) / results_per_page),
            'page_number': page_number,
            'results_per_page': results_per_page,
            'sort_by': sort_param,
            'filters': filter_params()
        }
    })

def search_people():
    result = []
    for filter_param in filter_params():
        if filter == 'email':
            result += filter(lambda person: flask.request.args.get('email') == person['email'], static_people)
        else:
            result += filter(lambda person: flask.request.args.get(filter_param) in person[filter_param], static_people)
        return result

def filter_params():
    return filter(lambda filter_param: filter_param in flask.request.args, ['first_name', 'last_name', 'email'])
