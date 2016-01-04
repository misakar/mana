mana
====
the missing startproject command for Flask <br/>

## What is mana
mana just like django startproject command, help you fast build and manage your flask project!

## Install mana
#### 1. install by pip

    $ pip install mana

#### 2. install from source

    $ git clone https://github.com/neo1218/mana
    $ cd mana
    $ sudo pip install .

## mana command set
### mana init (project_name)
![mana](http://7xj431.com1.z0.glb.clouddn.com/manamana2.gif) <br/>

<strong>mana init</strong> command can fast build a tiny flask app, which structure is:<br/>
![mana init](http://7xj431.com1.z0.glb.clouddn.com/manainit) <br/>
after init, you should install flask extensions(highly recommend use [virtualenv](http://flask.pocoo.org/docs/0.10/installation/#virtualenv)), just type <code>$ pip install -r requirement.txt</code> <br/>
you can run your project by <code>$ python manage.py runserver</code> <br/>
now, you can goto http://127.0.0.1:5000/test and check everything is ok :)

### mana startproject (project_name)

