from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import DBAPIError
# from ..models import MyModel
from gorna.models.mymodel import MyModel

from .tools import load_excel
@view_config(route_name='visual', renderer='../templates/visual.jinja2')
def my_view(request):
    print('=' * 40)
    print(request.params)
    file_path = './meta_xlsx/bk68.xlsx'
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
        return Response('', content_type='text/plain', status=500)

    return {'titles': data['title'], 'data': data['data']}

    # print('=*-*' * 40)
    # print(request.params)
    # file_path = './meta_xlsx/bk68.xlsx.json'
    # data = loadJson(file_path)
    # try:
    #     file_path = './meta_xlsx/bk68.xlsx.json'
    #     data = loadJson(file_path)
    #
    #     attr = []
    #     v1 = []  # 鱼类养殖面积
    #     v2 = []  # 海水养殖面积
    #     print(data[0]['省(市)名称'])
    #     for i in range(len(data)):
    #         attr.append(data[i]['采集年份'])
    #         # v1.append(data[i]['鱼类养殖面积'])
    #         v2.append(data[i]['海水养殖面积'])
    #         print(attr)
    #     line = Line("折线图-面积图示例")
    #     # line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
    #     line.add("北京", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
    #     #line.show_config()
    #     #line.render()
    #     print('=*-*' * 40)
    #     query = request.dbsession.query(MyModel)
    #     one = query.filter(MyModel.name == 'one').first()
    # except DBAPIError:
    #     return Response(db_err_msg, content_type='text/plain', status=500)

    return {'one': 'one','project': 'asd', }
# 可视化
