from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
from ..models import Rating
from sqlalchemy.exc import DBAPIError

from ..models.mymodel import MyModel

import os


@view_defaults(route_name='view_wiki_man')
class PostHist(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='../templates/wiki_hist/wiki_man_view.jinja2')
    def view(self):
        return


@view_defaults(route_name='edit_wiki_man')
class PostHist(object):
    def __init__(self, request):
        self.request = request

    @view_config(renderer='../templates/wiki_hist/wiki_man_edit.jinja2')
    def to_edit(self):
        return


@view_defaults(route_name='restore_wiki_man')
class PostHist(object):
    def __init__(self, request):
        self.request = request

    @view_config()
    def restore(self):
        return


@view_defaults(route_name='delete_wiki_man')
class PostHist(object):
    def __init__(self, request):
        self.request = request

    @view_config()
    def restore(self):
        return
