from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults
from sqlalchemy.exc import DBAPIError
# from ..models import MyModel
from gorna.models.mymodel import MyModel


@view_config(route_name='visual', renderer='../templates/visual.jinja2')
def my_view(request):
    print('=*-*' * 40)
    print(request.params)
    file_path = './meta_xlsx/bk68.xlsx.json'
    data = loadJson(file_path)
    try:
        file_path = './meta_xlsx/bk68.xlsx.json'
        data = loadJson(file_path)

        attr = []
        v1 = []  # 鱼类养殖面积
        v2 = []  # 海水养殖面积
        print(data[0]['省(市)名称'])
        for i in range(len(data)):
            attr.append(data[i]['采集年份'])
            # v1.append(data[i]['鱼类养殖面积'])
            v2.append(data[i]['海水养殖面积'])
            print(attr)
        line = Line("折线图-面积图示例")
        # line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
        line.add("北京", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
        #line.show_config()
        #line.render()
        print('=*-*' * 40)
        query = request.dbsession.query(MyModel)
        one = query.filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)

    return {'one': one,'project': 'asd', 'two': line.render()}
# 可视化
import json
from pyecharts import Line
def loadJson(path):
    f = open(path, encoding='utf-8')   # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    dada = json.load(f)
    dada1 = []
    for m in range(len(dada)):
        if (dada[m]['省(市)名称'] == '北京'):
            dada1.append(dada[m])
    return dada1
