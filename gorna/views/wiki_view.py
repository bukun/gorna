from pyramid.compat import escape
import re
from docutils.core import publish_parts

from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from ..models import Page

# regular expression used to find WikiWords
wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

'''
view_wiki() 
is the default view that gets called when a request is made to the root URL of our wiki. 
It always redirects to a URL which represents the path to our "FrontPage"
'''
@view_config(route_name='view_wiki')
def view_wiki(request):
    next_url = request.route_url('view_page', pagename='FrontPage')
    return HTTPFound(location=next_url)


'''
used to display a single page of our wiki.
'''
@view_config(route_name='view_page', renderer='../templates/view.jinja2',
             permission='view')
def view_page(request):
    page = request.context.page

    def add_link(match):
        word = match.group(1)
        exists = request.dbsession.query(Page).filter_by(name=word).all()
        if exists:
            view_url = request.route_url('view_page', pagename=word)
            return '<a href="%s">%s</a>' % (view_url, escape(word))
        else:
            add_url = request.route_url('add_page', pagename=word)
            return '<a href="%s">%s</a>' % (add_url, escape(word))

    content = publish_parts(page.data, writer_name='html')['html_body']
    content = wikiwords.sub(add_link, content)
    edit_url = request.route_url('edit_page', pagename=page.name)
    return dict(page=page, content=content, edit_url=edit_url)


'''
If the view execution is a result of a form submission, the view grabs the body element of the request parameters and 
sets it as the data attribute of the page object. It then redirects to the view_page view of the wiki page.
If the view execution is not a result of a form submission,the view simply renders the edit form, passing the page object
and a save_url which will be used as the action of the generated form.
'''
@view_config(route_name='edit_page', renderer='../templates/edit.jinja2',
             permission='edit')
def edit_page(request):
    page = request.context.page

    if 'form.submitted' in request.params:
        page.data = request.params['body']
        next_url = request.route_url('view_page', pagename=page.name)
        return HTTPFound(location=next_url)
    return dict(
        pagename=page.name,
        pagedata=page.data,
        save_url=request.route_url('edit_page', pagename=page.name),
        )


'''
 is invoked when a user clicks on a WikiWord which isn't yet represented as a page in the system
'''
@view_config(route_name='add_page', renderer='../templates/edit.jinja2',
             permission='create')
def add_page(request):
    pagename = request.context.pagename
    if 'form.submitted' in request.params:
        body = request.params['body']
        page = Page(name=pagename, data=body)
        page.creator = request.user
        request.dbsession.add(page)
        next_url = request.route_url('view_page', pagename=pagename)
        return HTTPFound(location=next_url)
    save_url = request.route_url('add_page', pagename=pagename)
    return dict(pagename=pagename, pagedata='', save_url=save_url)