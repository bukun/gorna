# gorna

自 1.8版本， scaffolds 被 cookieuffters 替代：


    pip install wheel
    pip install pyramid cookiecutter

pyramid-cookiecutter-starterURL dispatch for routing and either Jinja2,
Chameleon, or Mako for templatingpyramid-cookiecutter-alchemySQLite for persistent storage, 
SQLAlchemy for an ORM, URL dispatch for routing, 
and Jinja2 for templating.pyramid-cookiecutter-zodb
ZODB for persistent storage, traversal for routing, 
and Chameleon for templating



生成项目：

    cookiecutter gh:Pylons/pyramid-cookiecutter-starter

    cookiecutter gh:Pylons/pyramid-cookiecutter-alchemy

然后开始一些选项。

安装：

    pip install -e ".[testing]"

然后运行：

    initialize_gorna_db development.ini

   
注意，在数据库结构进行修改后，运行可能会有问题，这时要删除掉数据库文件，然后重新初始化数据库：

    rm gorna.sqlite
    initialize_gorna_db development.ini
    
开发环境中， 可以运行下面命令，修改过程可以自动加载重启：

    pserve development.ini --reload

下面是开始时开发时使用的简化代码：

    source ~/vpy_gorna/bin/activate
    cd github/gorna
    pserve development.ini --reload

