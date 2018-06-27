from pyramid.response import Response
from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home')
def home(request):
    return Response('<body>Visit <a href="/howdy">posts</a></body>')


# /howdy
@view_config(route_name='posts')
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')