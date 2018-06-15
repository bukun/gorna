import json
from texttable import Texttable


def loadJson(path):
    f = open(path, encoding='utf-8')   # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    dada = json.load(f)
    dada1 = []
    for m in range(len(dada)):
        if (dada[m]['林地面积'] >= 187):
            dada1.append(dada[m])
    return dada1
def showJson(data):
    table = Texttable()
    table.set_deco(Texttable.BORDER)
    table.set_cols_align(["l", "l", "l","l", "l", "l","l", "l", "l","l", "l", "l","l","l","l"])  # require three  columns
    table.set_cols_valign(["m", "m", "m","m", "m", "m","m", "m", "m","m", "m", "m","m", "m", "m"])
    table.set_cols_width([15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15])

    print(data)
    for i in range(len(data)):
        l = {}
       # print(type(l))
        for j in data[i]:
            #print((data[i][j]))
            #print(data[i][j])
            l[j] = data[i][j]
            #print(j, data[i][j])
        print(l.values())
        table.add_rows([l,l.values()])
    print(table.draw() + "\n")
if __name__ == '__main__':
    file_path = '/home/gislite/github/gorna/meta_xlsx/BB01.xlsx.json'
    data = loadJson(file_path)
    showJson(data)
