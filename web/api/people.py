# -*- coding: utf-8 -*-
"""
The people API
"""
import flask
from flask import jsonify
from flask import abort
from helpers import *

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
    for person in static_people:
        if person['id'] == person_id:
            return jsonify({'person': person})
        else:
            abort(404, {'message': 'Person not found'})


@blueprint.route('/')
def people_list():
    like_filters = filter_params(['first_name', 'last_name'])
    equal_filters = filter_params(['email'])

    sort_by = flask.request.args.get('sort_by')
    sort_direction = flask.request.args.get('sort_direction', default = 'asc', type = str)
    page_number = flask.request.args.get('page_number', default = 1, type = int)
    results_per_page = flask.request.args.get('results_per_page', default = 2, type = int)

    people = search_records(static_people, like_filters, equal_filters) or []
    people = sort_records(people, sort_by, reverse = True if sort_direction == 'desc' else False)

    total_pages = calc_total_pages(people, results_per_page)
    people_per_page = calc_records_on_page_number(people, page_number, results_per_page)

    return jsonify({
        'people': people_per_page,
        'meta_data': {
            'total_results': len(people),
            'total_pages': total_pages,
            'page_number': page_number,
            'results_per_page': results_per_page,
            'sort_by': sort_by,
            'sort_direction': sort_direction,
            'filters': like_filters + equal_filters,
            'iso_time': get_time()
        }
    })
