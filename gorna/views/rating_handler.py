from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from sqlalchemy.exc import DBAPIError

from ..models.mymodel import MyModel

import os


@view_defaults(route_name='_rating')
class PostViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = 'TutorialViews'


