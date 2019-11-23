import flask
import math

"""
Fetching
"""

def search_records(dict_list, like_filters = [], equal_filters = []):
    result = []
    if equal_filters:
        [result.extend(equal_filter(dict_list, value)) for value in equal_filters if equal_filters]
    else:
        [result.extend(like_filter(dict_list, value)) for value in like_filters if like_filters]
    return result

def filter_params(filter_list):
    return filter(lambda filter_param: filter_param in flask.request.args, filter_list)

"""
Filtering + Sorting
"""

def equal_filter(dict_list, value):
    return filter(lambda element: flask.request.args.get(value) == element[value], dict_list)

def like_filter(dict_list, value):
    return filter(lambda element: flask.request.args.get(value) in element[value], dict_list)

def sort_records(dict_list, sort_column):
    if sort_column and dict_list:
        return sorted(dict_list, key = lambda record: record[sort_column]) if sort_column and dict_list else []
    else:
        return dict_list

"""
Pagination
"""

def calc_total_pages(dict_list, results_per_page):
    return math.ceil(len(dict_list) / float(results_per_page))

def calc_records_on_page_number(dict_list, page_number, results_per_page):
    return list(split_list_in_chunks(dict_list, results_per_page))[page_number] if dict_list else []

def split_list_in_chunks(list, chunks):
    for i in xrange(0, len(list), chunks):
        yield list[i:i + chunks]
