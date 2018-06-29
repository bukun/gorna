from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
from ..models import Rating
from sqlalchemy.exc import DBAPIError

from ..models.mymodel import MyModel

import os


@view_config(route_name='view_post_man')
def view_post_man(request):
    return ''



@view_config(route_name='updatepost_rating')
def updatepost_rating(request):
    return ''


