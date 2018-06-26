from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from sqlalchemy.exc import DBAPIError

from ..models.mymodel import MyModel

import os


@view_defaults(route_name='post_view')
class PostViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'
        print('-' * 40)

    @property
    def full_name(self):
        first = self.request.matchdict['first']

        print('=' * 40)
        print(first)
        return first

    @view_config(renderer='../templates/posts/home.jinja2')
    def home(self):
        return {'page_title': 'Home View'}

    # Posting to /howdy/first/last via the "Delete" submit button
    @view_config(request_method='POST', request_param='form.delete', renderer='delete.pt')
    def delete(self):
        print('Deleted')
        return {'page_title': 'Delete View'}


@view_defaults(route_name='post_add')
class PostViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'
        print('-' * 40)

    # Retrieving /howdy/first/last the first time
    @view_config(renderer='../templates/posts/add.jinja2')
    def hello(self):
        return {'page_title': 'Hello View'}

    # Posting to /howdy/first/last via the "Edit" submit button
    @view_config(request_method='POST', renderer='../templates/posts/added.jinja2')
    def edit(self):
        new_name = self.request.params['new_name']
        return {'page_title': 'Edit View', 'new_name': new_name}
