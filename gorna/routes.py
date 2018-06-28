from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
)
from pyramid.security import (
    Allow,
    Everyone,
)

from .models import Page


def includeme(config):
    # ToDo: 按 TorCMS的路由，添加本项目路由。建立好 Handler 文件及 Class 。各方法为空即可。

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('datable', '/datable/{sig0}/{sig1}')
    config.add_route('post_add', '/post/_add')
    config.add_route('post_view', '/post/{sig0}')

    config.add_route('view_wiki', '/')

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')

    config.add_route('view_page', '/{pagename}', factory=page_factory)
    config.add_route('add_page', '/add_page/{pagename}', factory=new_page_factory)
    config.add_route('edit_page', '/{pagename}/edit_page', factory=page_factory)





    config.add_route('_rating', '/_rating/_update')







    '''begin'''
    config.add_route('news_list', '/post1/list')
    config.add_route('news_add', '/post1/add')
    config.add_route('news_add1', '/post1/add1')
    config.add_route('news_update', '/post1/update')
    '''end'''


def new_page_factory(request):
    pagename = request.matchdict['pagename']
    if request.dbsession.query(Page).filter_by(name=pagename).count() > 0:
        next_url = request.route_url('edit_page', pagename=pagename)
        raise HTTPFound(location=next_url)
    return NewPage(pagename)


class NewPage(object):
    def __init__(self, pagename):
        self.pagename = pagename

    def __acl__(self):
        return [
            (Allow, 'role:editor', 'create'),
            (Allow, 'role:basic', 'create'),
        ]


def page_factory(request):
    pagename = request.matchdict['pagename']
    page = request.dbsession.query(Page).filter_by(name=pagename).first()
    if page is None:
        raise HTTPNotFound
    return PageResource(page)


class PageResource(object):
    def __init__(self, page):
        self.page = page

    def __acl__(self):
        return [
            (Allow, Everyone, 'view'),
            (Allow, 'role:editor', 'edit'),
            (Allow, str(self.page.creator_id), 'edit'),
        ]
