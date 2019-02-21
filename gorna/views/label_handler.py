from pyramid.view import view_config
# from ..models.label import MPost2Label
import datetime


@view_config(route_name='label_remove')
def remove_redis_keyword(request):

    return


# @view_config(route_name='entity_view', renderer='../templates/list/label_list.jinja2')
# def list(request):
#     recs = request.dbsession.query(MPost2Label).all()
#     return {'recs': recs}