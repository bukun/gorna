# -*- coding=utf-8 -*-
import xlrd
import json
import codecs


def readExcel(path, name):
    # 打开excel表单
    excel = xlrd.open_workbook(path+name)
    # 得到第一张表单
    sheet1 = excel.sheets()[0]
    # 找到有几列几列
    nrows = sheet1.nrows  # 行数
    ncols = sheet1.ncols  # 列数
    totalArray = []
    title = []
    print(ncols)
    # 标题
    for i in range(0, ncols):
        title.append(sheet1.cell(5, i).value)
    print(title)
    # 数据
    for rowindex in range(9, nrows):
        dic = {}
        for colindex in range(0, ncols):
            s = sheet1.cell(rowindex, colindex).value
            dic[title[colindex]] = s
        totalArray.append(dic)
    data_json = json.dumps(totalArray, ensure_ascii=False, default="utf-8")
    return data_json

def saveFile(path, name, data):
    output = codecs.open(path + name + ".json", 'w', "utf-8")
    output.write(data)
    output.close()

if __name__ == '__main__':
    file_path = '/home/gislite/github/gorna/meta_xlsx/'
    file_name = 'bk68.xlsx'
    json_data = readExcel(file_path, file_name)
    saveFile(file_path, file_name, json_data)
