# -*- coding: utf-8 -*-
"""
The tasks API
"""
import flask
from flask import jsonify
from flask import abort
from helpers import *

blueprint = flask.Blueprint('tasks', __name__, url_prefix='/api/tasks')

static_tasks = [
    {
        'id': 1,
        'name': 'Clean up',
        'status': 'done'
    },
    {
        'id': 2,
        'name': 'Fix your car',
        'status': 'todo',

    },
    {
        'id': 3,
        'name': 'programming some Flask',
        'status': 'work in progress',
    }
]

@blueprint.route('/<int:task_id>')
def task_item(task_id):
    for task in static_tasks:
        if task['id'] == task_id:
            return jsonify({'task': task})
        else:
            abort(404, {'message': 'Task not found'})


@blueprint.route('/')
def tasks_list():
    like_filters = filter_params(['name'])
    equal_filters = filter_params(['status'])
    sort_param = flask.request.args.get('sort_by')
    sort_direction = str(flask.request.args.get('sort_direction'))
    page_number = int(flask.request.args.get('page_number')) if flask.request.args.get('page_number') else 0
    results_per_page = int(flask.request.args.get('results_per_page')) if flask.request.args.get('results_per_page') else 2

    tasks = search_records(static_tasks, like_filters, equal_filters) or []
    tasks = sort_records(tasks, sort_param, reverse = True if sort_direction == 'desc' else False)

    total_pages = calc_total_pages(tasks, results_per_page)
    tasks_per_page = calc_records_on_page_number(tasks, page_number, results_per_page)

    return jsonify({
        'tasks': tasks_per_page,
        'meta_data': {
            'total_results': len(tasks),
            'total_pages': total_pages,
            'page_number': page_number,
            'results_per_page': results_per_page,
            'sort_by': sort_param,
            'sort_direction': sort_direction,
            'filters': like_filters + equal_filters
        }
    })
