Pyramid Helloworld
2016年03月18日 09:45:19
阅读数：343
Pyramid 学习起航--------helloworld
英文文档在官网有！安装方法也在官网有详细说明！

链接http://docs.pylonsproject.org/projects/pyramid/en/1.6-branch/quick_tour.html有Pyramid概览文档，对Pyramid有初步认识。
直接上代码分析：
[python] view plain copy

    from wsgiref.simple_server import make_server  
    from pyramid.config import Configurator  
    from pyramid.response import Response  
      
      
    def hello_world(request):  
        return Response('Hello %(name)s!' % request.matchdict)  
      
    if __name__ == '__main__':  
        config = Configurator()  
        config.add_route('hello', '/hello/{name}')  
        config.add_view(hello_world, route_name='hello')  
        app = config.make_wsgi_app()  
        server = make_server('0.0.0.0', 8080, app)
        server.serve_forever()  
         

    首先Pyramid使用WSGI协议来web客户端应用和服务器。所以import wsgI的make_server。
    引入Pyramid 的配置类configurator，引入Pyramid关于HTTP response类
    hello_world是一个关键的view callable，“view callable”是一个关键的感念，链接中具体解释，它可以使一个类，一个函数，一个对象用作和客户端交互的主体，获取Http request，提供相应的response。

如果是一个函数的例子如下：
[python] view plain copy

    from pyramid.response import Response  
      
    class MyView(object):  
        def __init__(self, request):  
            self.request = request  
      
        def __call__(self):  
            return Response('hello')  

       4.if __name__ == '__main__':这个代码主要是分开两种情况：（1）当直接运行该py模块文件，Python helloworld.py会执行if条件下的代码，表示模块名字是main

          （2）当这个模块文件作为其他模块引用使用被import，那只有这个模块中的函数或类被调用，if条件后的代码不运行，因为模块名是helloworld。

           所以基本上这个是用作测试本模块代码的功能。

       5.configurator()函数用作生成Pyramid config配置对象，该对象可以进行应用配置，包括路由，ip，端口等信息，并且将应用进行注册到应用注册表。

       6.config.add_route('hello','/hello/{name}')   设置路由来匹配URL路径， config.add_view(hello_world,route_name='hello')设置view callable（类似设置回调函数）

       7.通过WSGI服务创建WSGI应用对象，该对象其实是一个Pyramid 路由的实例，它包含一个应用注册表的表项引用。

       8.最后开启WSGI server，监听web request请求。

 
