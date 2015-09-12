# coding: utf-8

"""
    mana
    ~~~~

        my flask toolkit & a command powered by click !

        mana init project_name                 # init your project
        mana install --venv/--no-venv          # install your flask extensions
        mana sql database_name                 # makesure the database_name is same with your config
        mana project_name app db               # create manage.py
        mana update project_name               # update the project
"""

import click
import os
from templates import _config_base, _config_with_sql, _file_init, \
                     _file_init_with_sql, _sql_models_file, _manage_py


def make_tuple(name, count):
    """格式化元组工厂函数"""
    format_tuple = []
    for i in range(count):
        format_tuple.append(name)
    return tuple(format_tuple)


def fill_file(project_name, filename, pre_code):
    """文件中填入预填代码"""
    path = os.popen('pwd').readlines()[0][0:-1]
    fo = open("%s/%s/%s" % (path, project_name, filename), "w+")
    fo.write(pre_code)
    fo.close


@click.group()
def mana():
    """my flask toolkit
       help me generate my flask app"""
    pass


@mana.command()
@click.argument('project_name', default="my_project")
def init(project_name):
    """init your project"""
    # just like shell !
    # create folders and files
    os.system("mkdir %s" % project_name)
    os.system("touch %s/README.md %s/config.py %s/requirement.txt" \
            % make_tuple(project_name, 3))
    os.system("mkdir %s/app/ %s/test/" \
            % make_tuple(project_name, 2))
    os.system("touch %s/app/__init__.py %s/app/models.py %s/app/views.py %s/app/forms.py" % \
            make_tuple(project_name, 4))
    os.system("mkdir %s/app/templates/ %s/app/static/" % \
            make_tuple(project_name, 2))
    os.system("cd ..")

    # happy coding
    fill_file(project_name,'config.py', _config_base)
    fill_file(project_name,'app/__init__.py', _file_init)

    click.echo("init ... done!")


@mana.command()
@click.option('--venv/--no-venv', default=False, help="")
def install(venv):
    """install your flask extensions"""
    if venv:
        click.echo("creating venv")
        os.system("virtualenv venv")
        os.system(". venv/bin/activate")

        click.echo("install extensions")
        os.system("pip install -r requirement.txt")
        click.echo("install ... done!")
    else:
        click.echo("install extensions")
        os.system("pip install -r requirement.txt")
        click.echo("install ... done!")


@mana.command()
@click.argument('project_name')
def sql(project_name):
    """integrate flask-sqlalchemy"""
    fill_file(project_name, 'config.py', _config_with_sql)
    fill_file(project_name, 'app/__init__.py', _file_init_with_sql)
    fill_file(project_name, 'app/models.py', _sql_models_file)
    click.echo("integrate flask-sqlalchemy ... done!")


@mana.command()
@click.argument('project_name')
def manage(project_name):
    """create manage.py help me:)"""
    fill_file(project_name, 'manage.py', _manage_py)
    click.echo("create ... done!")

