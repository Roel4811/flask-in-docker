# -*- coding: utf-8 -*-
"""
The tasks API
"""
import flask
from flask import jsonify
from flask import abort
import math

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
    tasks = search_tasks() or [] # """ implement search_records """

    sort_param = flask.request.args.get('sort_by')
    page_number = int(flask.request.args.get('page_number')) or 0
    results_per_page = int(flask.request.args.get('results_per_page')) or 1
    total_pages = math.ceil(len(tasks) / float(results_per_page))

    tasks = sorted(tasks, key = lambda task: task[sort_param]) if sort_param else tasks
    tasks_split_per_page = list(split_list_in_chunks(tasks, results_per_page))
    tasks_per_page = tasks_split_per_page[page_number] if tasks else []

    return jsonify({
        'tasks': tasks_per_page,
        'meta_data': {
            'total_results': len(tasks),
            'total_pages': total_pages,
            'page_number': page_number,
            'results_per_page': results_per_page,
            'sort_by': sort_param,
            'filters': filter_params()
        }
    })


def split_list_in_chunks(list, chunks):
    for i in xrange(0, len(list), chunks):
        yield list[i:i + chunks]

def search_tasks():
    result = []
    for filter_param in filter_params():
        if filter == 'status':
            result += filter(lambda task: flask.request.args.get('status') == task['status'], static_tasks)
        else:
            result += filter(lambda task: flask.request.args.get(filter_param) in task[filter_param], static_tasks)
            return result

def filter_params():
    return filter(lambda filter_param: filter_param in flask.request.args, ['name', 'status'])
