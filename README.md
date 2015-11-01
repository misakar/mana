mana
===
![mana](http://7xj431.com1.z0.glb.clouddn.com/images.jpeg)
### happy🍺 generate flask project

### 为什么要使用mana ?
#### 1. I Don't Want Waste Time on --mkdir--
#### 2. I Don't Want [virtualenv venv] [. venv/bin/activate] and [ pip pip pip...]
#### 3. I Don't Want [from flask.ext.xxx import Xxx] [xxx = Xxx(app)]
#### 4. I Don't Want [blue = Blueprint('blue'..)] [app.register_blueprint('blue', url_prefix="/blue")]

            ..................So..........Use.........mana...................

<h2>Features, usage and installation instructions are summarised on [the homepage](http://121.43.230.104:520/mana).</h2><br/>


## 对mana的思考

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
    ----------------------------------------------------
    2015-1030: fix ISSUE #3 && happy🍺agenerate flask project
    ----------------------------------------------------
    2015-1030: delete sql and add --sql --config to init
    ----------------------------------------------------
    2015-1030: update README + upload mana2.2 to PyPi !!!!
    ----------------------------------------------------
    2015-1030: update mana init --> yes we can run!!!!
    ----------------------------------------------------
    2015-1031: add mana homepage!!!
    ----------------------------------------------------
    2015-1031: mana2.5 fix issue #8


## powered by click
[click源码](https://github.com/mitsuhiko/click) 😄  <br/>

    click 是flask作者的一个开源项目
    flask 作者是我的偶像😼

[click文档](http://click.pocoo.org/5/)👌 <br/>
