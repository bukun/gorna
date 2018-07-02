from pyramid.view import view_config
from ..models.post import Post
import datetime


@view_config(route_name='admin', renderer='../templates/admin/admin_index.jinja2')
def view_list(request):
    news = request.dbsession.query(Post).all()
    return {'news': news, 'new_name': '123'}



