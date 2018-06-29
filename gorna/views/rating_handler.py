from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
from ..models import Rating
from sqlalchemy.exc import DBAPIError

from ..models.mymodel import MyModel

import os

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from sqlalchemy.exc import DBAPIError

from ..models.mymodel import MyModel

import os


@view_defaults(route_name='update_rating')
class Rating(object):
    def __init__(self, request):
        self.request = request


    @view_config(request_method='POST', renderer='')
    def update_rating(self):

        return



@view_defaults(route_name='updatepost_rating')
class Rating(object):
    def __init__(self, request):
        self.request = request

    @view_config(request_method='POST', renderer='')
    def update_post(self):

        return