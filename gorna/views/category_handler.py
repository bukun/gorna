from pyramid.view import view_config
from ..models.entity import Entity
import datetime


@view_config(route_name='category_list', renderer='../templates/list/list.jinja2')
def view_list(request):
    recs = request.dbsession.query(Entity).all()
    return {'recs': recs}
