from pyramid.view import view_config
from ..models.entity import Entity
import datetime


@view_config(route_name='entity_list', renderer='../templates/entity/entity_list.jinja2')
def view_list(request):
    recs = request.dbsession.query(Entity).all()
    return {'recs': recs}


@view_config(route_name='entity_add', request_method='GET', renderer='../templates/entity/entity_add.jinja2')
def add(request):
    add_url = request.route_url('entity_add')
    return {'add_url': add_url}


@view_config(route_name='news_add1', renderer='../templates//entity/entity_list.jinja2')
def add1(request):
    new = Entity()
    new.title = request.params['path']
    new.content = request.params['desc']
    new.time_create = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    request.dbsession.add(new)
    rec = request.dbsession.query(Entity).all()
    return {'rec': rec}


@view_config(route_name='news_update', renderer='../templates/news_list.jinja2')
def update(request):
    from json import loads
    body = request.body.decode()
    json = loads(body, encoding=request.charset)
    #  request.json_body
    title = json['title']
    content = json['content']
    uid = json['uid']
    news_result = request.dbsession.query(Entity).filter_by(uid=uid).first()
    news_result.title = title
    news_result.content = content
    #request.dbsession.commit()
    news = request.dbsession.query(Entity).all()
    return {'news': news}


