'''
Single-File Web Applications
'''

from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    '''
    Implement the view code that generates the response.
    '''
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')


if __name__ == '__main__':
    # Use Pyramid's configurator in a context manager to connect view code to a particular URL route.
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    # Publish a WSGI app using an HTTP server.
    serve(app, host='0.0.0.0', port=6543)
