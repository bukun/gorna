import web
import json
import sys





def loadJson(path):
    f = open(path, encoding='utf-8')   # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    dada = json.load(f)
    dada1 = []
    for m in range(len(dada)):
        if (dada[m]['省(市)名称'] == '北京'):
            dada1.append(dada)
    return dada1




urls = (
    '/(.*)', 'hello'
)

app = web.application(urls, globals())


class hello:
    def GET(self, name):
        web.header('Content-Type', 'text/html;charset=UTF-8')
        file_path = '/home/gislite/github/gorna/meta_xlsx/bk68.xlsx.json'
        dataa = loadJson(file_path)

        print(dataa)
        return dataa
if __name__ == "__main__":
    app.run()