from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from sqlalchemy.exc import DBAPIError

from ..models import MyModel

import os


# One route, at /howdy/amy, so don't repeat on each @view_config
@view_defaults(route_name='hello')
class HelloWorldViews:
    def __init__(self, request):
        self.request = request
        # Our templates can now say {{ view.name }}
        self.name = request.matchdict['name']

    # Retrieving /howdy/amy the first time
    @view_config(renderer='hello.jinja2')
    def hello_view(self):
        return dict()

    # Posting to /howdy/amy via the "Edit" submit button
    @view_config(request_param='form.edit', renderer='edit.jinja2')
    def edit_view(self):
        print('Edited')
        return dict()

    # Posting to /howdy/amy via the "Delete" submit button
    @view_config(request_param='form.delete', renderer='delete.jinja2')
    def delete_view(self):
        print('Deleted')
        return dict()


@view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
def my_view(request):
    print('=' * 40)
    print(request.params)

    inws = './meta_xlsx'
    # xlsx_files = []
    # for wroot, wdirs, wfiles in os.walk(inws):
    #     for wfile in wfiles:
    #         if wfile.lower().endswith('.xlsx'):
    #             xlsx_files.append()
    #

    all_files = []
    for uuvv in os.listdir(inws):
        xlsx_files = []
        the_path = os.path.join(inws, uuvv)
        if os.path.isdir(the_path):
            for ttt in os.listdir(the_path):
                if ttt.lower().endswith('.xlsx'):
                    xlsx_files.append([ttt, os.path.join(uuvv, ttt)])
            all_files.append([uuvv, xlsx_files])

    print(all_files)
    try:
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'one': one, 'project': 'gorna', 'all_files': all_files}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_gorna_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
