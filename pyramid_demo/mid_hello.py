from wsgiref.simple_server import make_server  
from pyramid.config import Configurator  
from pyramid.response import Response  
  
  
def hello_world(request):  
    return Response('Hello %(name)s!' % request.matchdict)  
  
if __name__ == '__main__':  
    config = Configurator()  
    config.add_route('posts', '/posts/{name}')
    config.add_view(hello_world, route_name='posts')
    app = config.make_wsgi_app()  
    server = make_server('0.0.0.0', 8080, app)  
    server.serve_forever()
