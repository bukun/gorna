from pyramid.view import view_config
from ..models.entity import Entity
import datetime
import uuid

@view_config(route_name='entity_list', renderer='../templates/entity/entity_list.jinja2')
def view_list(request):
    recs = request.dbsession.query(Entity).all()

    return {'recs': recs}


@view_config(route_name='entity_add', request_method='GET', renderer='../templates/entity/entity_add.jinja2')
def add(request):
    add_url = request.route_url('entity_add')
    return {'add_url': add_url}


@view_config(route_name='entity_add1', renderer='../templates/entity/entity_list.jinja2')
def add1(request):
    new = Entity()
    new.uid = 'scscscscscscsc'

    new.path = request.params['path']
    new.desc = request.params['desc']
    new.time_create = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    request.dbsession.add(new)
    recs = request.dbsession.query(Entity).all()
    return {'recs': recs}


@view_config(route_name='entity_down')
def down(request):
    return


@view_config(route_name='entity_view', renderer='../templates/entity/entity_view.jinja2')
def view_list(request):
    recs = request.dbsession.query(Entity).all()
    return {'recs': recs}
