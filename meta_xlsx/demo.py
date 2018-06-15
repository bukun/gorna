'''
from texttable import Texttable

table = Texttable()

table.set_deco(Texttable.BORDER)
table.set_cols_align(["l", "l", "l"])#require three  columns
table.set_cols_valign(["m", "m", "m"])
table.set_cols_width([10,5,10,20])


table.add_rows([ #["Name", "Age", "Nickname"],
             #["Mr\nXavier\nHuon", 32, "Xav'"],
             #["Mr\nBaptiste\nClement", 1, "Baby"] ,
         ["Tom",32,"cat"],
         ["ancj",9,"hjasdg"],
         ["asdhjaskhd",109,"nash"]  ])
print(table.draw() + "\n")

from pyecharts import Bar
bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
bar.show_config()
bar.render()

from pyecharts import Bar

attr = ['牧草地面积', '水田面积', '林地面积', '耕地面积', '采集年份', '土地总面积KM2', '居民点及工矿用地', '土地总面积']
#v1 = [ 0.32, 11.01, 0.49, 99999999.99, 99999999.99, 0.59, '130601', 1986.0]
bar = Bar("图表主标题", "图表副标题")
#bar.add("保定市", attr, v1)
#bar.add("清苑", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
bar.render()

from pyecharts import Line3D
from pyecharts import Line

line =Line("折线图-面积图示例")
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
line.show_config()
line.render()
'''
import json
from pyecharts import Line


def loadJson(path):
    f = open(path, encoding='utf-8')  # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    dada = json.load(f)
    dada1 = []
    for m in range(len(dada)):
        if (dada[m]['省(市)名称'] == '北京'):
            dada1.append(dada[m])
    return dada1


def showJson(data):
    attr = []
    v1 = []  # 鱼类养殖面积
    v2 = []  # 海水养殖面积
    print(data[0]['省(市)名称'])
    for i in range(len(data)):
        print(data[i])
        attr.append(data[i]['采集年份'])
        v1.append(data[i]['鱼类养殖面积'])
        v2.append(data[i]['海水养殖面积'])
        for j in data[i]:
            print('-------------------' + j)
        print(attr)
    line = Line("折线图-面积图示例")
    line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
    line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
    # line.show_config()
    line.render()


if __name__ == '__main__':
    file_path = '/home/gislite/github/gorna/meta_xlsx/bk68.xlsx.json'
    data = loadJson(file_path)
    showJson(data)

# web显示表格可以分组 之后可视化
