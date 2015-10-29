mana
===
![mana](http://7xj431.com1.z0.glb.clouddn.com/images.jpeg)
### fast generate flask project

### 为什么要使用mana ?
#### 1. I Don't Want Waste Time on --mkdir--
#### 2. I Don't Want [virtualenv venv] [. venv/bin/activate] and [ pip pip pip...]
#### 3. I Don't Want [from flask.ext.xxx import Xxx] [xxx = Xxx(app)]
#### 4. I Don't Want [blue = Blueprint('blue'..)] [app.regist_blueprint('blue', url_prefix="/blue")]

            ..................So..........Use.........mana...................


## 使用mana:
### 1. mana init --> 构建你的项目

    ~> mana init my_project

你已经创建了你的目录结构(如图)<br/>

                    |-app/              ---- __init__.py
                    |-test/                  models.py
    my_project   -  |-config.py              views.py
                    |-requirement.txt        forms.py
                    |-README.md              templates
                    |                        static

并且在相关文件中预填了代码<br/>
[config.py预填代码](https://github.com/neo1218/mana/blob/master/examples/GoodIdea/config.py) : 三个配置类, 对应生产、测试、开发环境配置 <br/>
[app/__init__.py预填代码](https://github.com/neo1218/mana/blob/master/examples/GoodIdea/app/__init__.py) : 创建了flask app, 导入了基本配置

### 2. mana install (--venv) --> 安装flask扩展
在 requirement.txt 中写入你希望安装的扩展的名称 <br/>
ex:

    flask==0.10
    click
    mana

进入与requirement文件同级的目录然后运行安装命令

    $ mana install --venv

这个命令会自动创建并进入虚拟环境,将requirement文件中的扩展安装在该环境中<br/>
如果你希望在全局环境中安装扩展，你可以不使用--venv 选项

    $ mana install

这样你的扩展就会被安装到全局中<br/>
不过强烈建议使用使用虚拟环境进行开发,参见[virtualenv](http://docs.jinkan.org/docs/flask/installation.html#virtualenv) <br/>


### 3. mana sql --> 集成 flask-sqlalchemy 处理关系型数据库
对于sql数据库的处理, flask-sqlalchemy 是我最常用的扩展，使用mana可以快速集成flask-sqlalchemy并初始化扩展

    进入与项目根目录同级的目录 🍺
    $ mana sql project_name

接下来，你只需要专心于models.py的数据库类设计与编码了<br/>


### 4. mana manage --> 使用 manage.py 管理你的项目
还可以使用mana创建manage.py集成flask-script和flask-migrate管理我们的项目

    进入与项目根目录同级的目录 🍺
    $ mana manage project_name

现在可以使用manage.py进行数据库迁移和更新了

    $ python manage.py db init
    $ python manage.py db migrate -m "v1.0"
    $ python manage.py db upgrade

使用manage.py启动服务器(运行项目)

    $ python manage.py runserver

使用shell环境

    $ python manage.py shell

配置shell环境 <br/>
如果你希望在shell中自动导入模块(ex: 导入User)的话:

    from app.models import User

    def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app,
        db=db,
        User=User
    )

效果:

    python manage.py shell
    >> User
    <class 'app.models.User'>

### 5. mana blue (--prefix)--> 自动注册蓝图

    进入与项目根目录同级的目录 🍺
    $ mana blue project_name bluep

这样你就创建了一个叫bluep的蓝图,并在app中注册 <br/>
你也可以配置蓝图的url前缀

    $ mana blue project_name bluep --prefix="/bluep"

这样就可以通过 /bluep/... 去访问蓝图对应的视图

### 6. mana deploy --> deploy flask application on wsgi server

    进入与项目根目录同级的目录 🍺
    $ mana deploy project_name --host=121.43.230.104 --port=2333

这样就可以创建wsgi.py去部署你的flask应用

### 7. mana what? --> use your imagination ..

    未完 .... 待续 ....

## mana 的坏处

    mana最大的好处就是方便、减少重复、快速
    但是为了以上这些 mana 放弃了自由 --> 不得不固定的使用某些特定的扩展
    每个flask开发者的工具集可能都不一样，mana不一定适合所有人。
    所以mana个人感觉还是自己用的顺手些。


## my flask toolkit
处理sql数据库: [flask-sqlalchemy](https://github.com/mitsuhiko/flask-sqlalchemy)<br/>
处理登录: [flask-login](https://github.com/maxcountryman/flask-login)<br/>
进行数据库迁移: [flask-migrate](https://github.com/miguelgrinberg/Flask-Migrate)<br/>
进行项目管理: [flask-script](https://github.com/smurfix/flask-script)<br/>
后台管理: [flask-admin](https://github.com/flask-admin/flask-admin)<br/>


## future
1. 自动处理登录<br/>
2. init 更加细化: 单文件，无蓝图组织，蓝图组织<br/>
3. 自动添加测试单元<br/>


## 进度

	2015-0910: have an idea
	----------------------------------------------------
	2015-0911: mana init & mana install & mana sql
	----------------------------------------------------
	2015-0912: mana manage
	----------------------------------------------------
	2015-0920: clean this repo..
	----------------------------------------------------
	2015-1024: hackathon hack
	----------------------------------------------------
	2015-1024: mana init update, review my old code :(
    ----------------------------------------------------
    2015-1028: complete mana blue, but not test...
    ----------------------------------------------------
    2015-1028: rewrite README for more detail
    ----------------------------------------------------
    2015-1029: add mana deploy to deploy flask app on wsgi server



## powered by click
[click源码](https://github.com/mitsuhiko/click) 😄  <br/>

    click 是flask作者的一个开源项目
    flask 作者是我的偶像😼

[click文档](http://click.pocoo.org/5/)👌 <br/>
