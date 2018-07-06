from pyramid.view import view_config
from ..models.entity2user import Entity2User


@view_config(route_name='entity_download', renderer='../templates/entity/entity_download.jinja2')
def all_list(request):
    recs = request.dbsession.query(Entity2User).all()
    return {'recs': recs}


@view_config(route_name='entity_user_download', renderer='../templates/entity/entity_user_download.jinja2')
def user_list(request):
    recs = request.dbsession.query(Entity2User).all()
    return {'recs': recs}