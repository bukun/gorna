'''
Python Packages for Pyramid Applications
Most modern Python development is done using Python packages, an approach Pyramid puts to good use.
In this step we redo "Hello World" as a minimal Python package inside a minimal Python project.
'''
from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('posts', '/')
        config.add_view(hello_world, route_name='posts')
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)
