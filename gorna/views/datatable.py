from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import DBAPIError
from ..models import MyModel
import json
import openpyxl
from .tools import load_excel
@view_config(route_name='datable', renderer='../templates/datable.jinja2')
def my_view(request):
    print('=' * 40)
    print(request.params)

    sig0 = request.matchdict['sig0']
    sig1 = request.matchdict['sig1']

    file_path = './meta_xlsx/{sig0}/{sig1}'.format(sig0 = sig0, sig1 = sig1)
    print(file_path)

    data = load_excel(file_path)
    try:
        pass
        # thead = []
        # tbody = []
        # v2 = []
        # for i in range(len(data)):
        #     v1 = []
        #     for j in data[i]:
        #         if i == 0:
        #             v2.append(j)
        #         # print(j,data[i][j])
        #         v1.append(data[i][j])
        #     tbody.append(v1)
        # thead.append(v2)
        # print(thead)
        # print(tbody)
        # query = request.dbsession.query(MyModel)
        # one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return data


    #
    # f = open(path, encoding='utf-8')   # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    # dada = json.load(f)
    # dada1 = []
    # for m in range(len(dada)):
    #     if (dada[m]['省(市)名称'] != '北京'):
    #         dada1.append(dada[m])
    # return dada1
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
