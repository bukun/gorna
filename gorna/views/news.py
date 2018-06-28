from pyramid.view import view_config
from ..models.post import Post
import datetime


@view_config(route_name='news_list', renderer='../templates/news_list.jinja2')
def view_list(request):
    news = request.dbsession.query(Post).all()
    return {'news': news, 'new_name': '123'}


@view_config(route_name='news_add', request_method='GET', renderer='../templates/news_add.jinja2')
def add(request):
    add_url = request.route_url('news_add1')
    return {'add_url': add_url}


@view_config(route_name='news_add1', renderer='../templates/news_list.jinja2')
def add1(request):
    new = Post()
    new.title = request.params['title']
    new.content = request.params['content']
    new.time_create = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new.time_update = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    request.dbsession.add(new)
    news = request.dbsession.query(Post).all()
    return {'news': news}


@view_config(route_name='news_update', renderer='../templates/news_list.jinja2')
def update(request):
    from json import loads
    body = request.body.decode()
    json = loads(body, encoding=request.charset)
    #  request.json_body
    title = json['title']
    content = json['content']
    uid = json['uid']
    news_result = request.dbsession.query(Post).filter_by(uid=uid).first()
    news_result.title = title
    news_result.content = content
    #request.dbsession.commit()
    news = request.dbsession.query(Post).all()
    return {'news': news}


