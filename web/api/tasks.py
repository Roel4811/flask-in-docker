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
            return jsonify(task)
        else:
            abort(404, {'message': 'Task not found'})


@blueprint.route('/')
def tasks_list():
    like_filters = filter_params(['name'])
    equal_filters = filter_params(['status'])
    sort_param = str(flask.request.args.get('sort_by'))
    page_number = int(flask.request.args.get('page_number')) or 0
    results_per_page = int(flask.request.args.get('results_per_page')) or 1

    tasks = search_records(static_tasks, like_filters, equal_filters) or []
    tasks = sort_records(tasks, sort_param)

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
            'filters': like_filters + equal_filters
        }
    })
