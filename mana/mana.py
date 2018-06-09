# coding: utf-8

"""
mana
~~~~
the missing startproject command for flask

Usage:

    mana init <project_name>

    mana startproject <project_name>

    mana blueprint <blueprint_name>

    mana version   show version

Options:

    mana --help:    help information

Install:

    $ pip install mana (--upgrade)

"""

import os

# operators
from operators import _mkdir_p
from operators import init_code

# templates
from templates.manage import _manage_basic_code, _manage_admin_code,_manage_rest_code
from templates.requirement import _requirement_code, _requirement_admin_code,_rest_requirement_code
from templates.views import _views_basic_code, _views_blueprint_code
from templates.forms import _forms_basic_code
from templates.init import _init_basic_code, _init_blueprint_code, \
                           _init_admin_code, _rest_main_init_code, \
                            _rest_init_blueprint_code,_rest_util_init_code
from templates.config import _config_sql_code
from templates.models import _models_admin_code,_rest_models_code
from templates.admin import _admin_views_code, _admin_index_html_code, \
                            _admin_logout_html_code
from templates.auth import _auth_forms_code, _auth_views_code, \
                           _auth_login_html_code, _auth_login_css_code, \
                            _rest_auth_code
from templates.decorators import _rest_decorators_code
from templates.handler import _rest_user_handler_code
from templates.utils import _util_pagenation_code
from templates.tests import _rest_test_code

# logging
import logging
from logging import StreamHandler, DEBUG
# logger
logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())


# logging info
def warning_path_exist(path):
    """
    send warning msg if path exist
    """
    logger.warning('''\033[31m{Warning}\033[0m
    ==> \033[32m%s\033[0m\n exist
    ==> please change the project name,
    ==> and try again !''' % path)


def start_init_info(path):
    """
    start init msg
    """
    if os.path.isdir(path):
        warning_path_exist(path)
        exit(1)
    else:
        logger.info('''\033[33m{Info}\033[0m
    ==> start init your flask project [on]
    ==> \033[32m%s\033[0m\n''' % path)


def init_done_info():
    """
    init done
    """
    logger.info('''\033[33m{Info}\033[0m
    ==> init your flask project done !''')


# create
def create_templates_static_files(app_path):
    """
    create templates and static
    """
    templates_path = os.path.join(app_path, 'templates')
    static_path = os.path.join(app_path, 'static')
    _mkdir_p(templates_path)
    _mkdir_p(static_path)
    # create {img, css, js}
    os.chdir(static_path)
    img_path = os.path.join(static_path, 'img')
    css_path = os.path.join(static_path, 'css')
    js_path = os.path.join(static_path, 'js')
    _mkdir_p(img_path)
    _mkdir_p(css_path)
    _mkdir_p(js_path)

    return css_path, templates_path


def create_blueprint(app_path, blueprint, views_code, forms_code, templates_path):
    """
    create blueprint
    """
    blueprint_path = os.path.join(app_path, blueprint)
    _mkdir_p(blueprint_path)
    # create  blueprint files
    os.chdir(blueprint_path)
    init_code('__init__.py', _init_blueprint_code % (blueprint, blueprint))
    init_code('views.py', views_code)
    init_code('forms.py', forms_code)
    # main blueprint templates
    os.chdir(templates_path)
    blueprint_templates_path = os.path.join(templates_path, blueprint)
    _mkdir_p(blueprint_templates_path)

    return blueprint_templates_path


"""use click:)"""
import click


@click.group()
def cli():
    """
    the missing startproject command for Flask

    \b
    [processes]
    virtualenv venv
    && source venv/bin/activate     -> create a virtual environment (optional)
    pip install -r requirement.txt  -> install flask extensions

    \b
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade     -> setup sql database(default database is sqlite)

    \b
    python manage.py shell          -> create roles
    >> Role.insert_roles()
    >> quit()

    \b
    python manage.py admin          -> create admin user
    python manage.py runserver(-d)  -> run project(in debug mode)'''
    """
    pass


@click.command()
@click.argument('project_name')
def init(project_name):
    """
    build a minimal flask project
    """
    # the destination path
    dst_path = os.path.join(os.getcwd(), project_name)

    start_init_info(dst_path)

    # create dst path
    _mkdir_p(dst_path)

    os.chdir(dst_path)
    # create files
    init_code('manage.py', _manage_basic_code)
    init_code('requirement.txt', _requirement_code)

    # create app/
    app_path = os.path.join(dst_path, 'app')
    _mkdir_p(app_path)

    os.chdir(app_path)
    # create files
    init_code('views.py', _views_basic_code)
    init_code('forms.py', _forms_basic_code)
    init_code('__init__.py', _init_basic_code)

    create_templates_static_files(app_path)

    init_done_info()


@click.command()
@click.argument('blueprint_name')
def blueprint(blueprint_name):
    """
    create and register a blueprint
    """
    app = os.getcwd().split('/')[-1]
    if app != 'app':
        logger.warning('''\033[31m{Warning}\033[0m
==> your current path is \033[32m%s\033[0m\n
==> please create your blueprint under app folder!''' % os.getcwd())
        exit(1)

    # destination path
    dst_path = os.path.join(os.getcwd(), blueprint_name)
    if os.path.isdir(dst_path):
        logger.warning('''\033[31m{Warning}\033[0m
==> bluprint \033[32m%s\033[0m\n exist
==> please try again !''' % dst_path)
        exit(1)

    # create dst_path
    _mkdir_p(dst_path)

    # change dir
    os.chdir(dst_path)
    # create files
    init_code('__init__.py', _init_blueprint_code %
        (blueprint_name, blueprint_name))
    init_code('views.py', _views_blueprint_code %
        (blueprint_name, blueprint_name))
    init_code('forms.py', _forms_basic_code)

    # register auth in app
    os.chdir(os.path.join(dst_path, '..'))
    with open('__init__.py', 'r+') as f:
        prev = pos = 0
        while f.readline():
            prev, pos = pos, f.tell()
        f.seek(prev)
        f.write(
            '\nfrom %s import %s\napp.register_blueprint(%s, url_prefix="/%s")\n\n'
            % (
                blueprint_name, blueprint_name,
                blueprint_name, blueprint_name
            )
        )

    # create blueprint templates
    templates_path = os.path.join(os.getcwd(), 'templates')
    os.chdir(templates_path)
    blueprint_templates_path = os.path.join(templates_path, blueprint_name)
    _mkdir_p(blueprint_templates_path)

    logger.info('''\033[33m{Info}\033[0m: create blueprint done!''')


@click.command()
@click.argument('project_name')
def startproject(project_name):
    """
    build a full status project
    """
    # the destination path
    dst_path = os.path.join(os.getcwd(), project_name)
    start_init_info(dst_path)

    # create dst path
    _mkdir_p(dst_path)

    # create project tree
    os.chdir(dst_path)
    # create files
    init_code('manage.py', _manage_admin_code)
    init_code('requirement.txt', _requirement_admin_code)
    init_code('config.py', _config_sql_code)

    # create app/
    app_path = os.path.join(dst_path, 'app')
    _mkdir_p(app_path)

    # create files
    os.chdir(app_path)
    init_code('models.py', _models_admin_code)
    init_code('__init__.py', _init_admin_code)

    # create templates and static
    css_path, templates_path = create_templates_static_files(app_path)
    # create css files
    os.chdir(css_path)
    init_code('sign.css', _auth_login_css_code)

    # create main blueprint
    create_blueprint(
        app_path,
        'main',
        _views_blueprint_code % ('main', 'main'),
        _forms_basic_code,
        templates_path
    )

    # create auth blueprint
    auth_templates_path = create_blueprint(
        app_path,
        'auth',
        _auth_views_code,
        _auth_forms_code,
        templates_path
    )
    # create auth templates files
    os.chdir(auth_templates_path)
    init_code('login.html', _auth_login_html_code)

    # create admin site
    admin_path = os.path.join(app_path, 'admin')
    _mkdir_p(admin_path)

    # create admin files
    os.chdir(admin_path)
    init_code('__init__.py', '')
    init_code('views.py', _admin_views_code)

    # create admin templates
    os.chdir(templates_path)
    admin_templates_path = os.path.join(templates_path, 'admin')
    _mkdir_p(admin_templates_path)

    # create admin templates files
    os.chdir(admin_templates_path)
    init_code('index.html', _admin_index_html_code)
    init_code('logout.html', _admin_logout_html_code)

    init_done_info()


@click.command()
@click.argument('module')
def admin(module):
    """add sql modules into admin site"""
    # add module into admin site
    app = os.getcwd().split('/')[-1]
    if app != 'app':
        logger.warning('''\033[31m{Warning}\033[0m
==> your current path is \033[32m%s\033[0m\n
==> please add your sql module under app folder!''' % os.getcwd())
        exit(1)

    admin_path = os.path.join(os.getcwd(), 'admin')
    os.chdir(admin_path)
    with open('views.py', 'r+') as f:
        prev = pos = 0
        while f.readline():
            prev, pos = pos, f.tell()
        f.seek(prev)
        f.write(
            '\nfrom app.models import %s\nadmin.add_view(ModelView(%s, db.session))'
            % (module, module)
        )

    logger.info('''\033[33m{Info}\033[0m: add module done!''')


@click.command()
def version():
    """mana version"""
    click.echo("mana version: 4.9 \/ ")


@click.command()
@click.argument('project_name')
def rest_startproject(project_name):
    """start a restful flask project"""
    # the destination path
    dst_path = os.path.join(os.getcwd(), project_name)

    start_init_info(dst_path)

    # create dst path
    _mkdir_p(dst_path)

    os.chdir(dst_path)

    # create files under dst_path
    init_code('manage.py', _manage_rest_code)
    init_code('requirement.txt', _rest_requirement_code)
    init_code('config.py',_config_sql_code)

    # create app/ dic under dst_path
    app_path = os.path.join(dst_path, 'app')
    _mkdir_p(app_path)

    os.chdir(app_path)
    # create files under app path
    init_code('models.py', _rest_models_code)
    init_code('decorators.py', _rest_decorators_code)
    init_code('__init__.py', _rest_main_init_code)

    # create api/ dir under app_path
    api_path = os.path.join(app_path, "api")
    _mkdir_p(api_path)

    os.chdir(api_path)
    # create files under api_v1.0/ dir
    init_code("auth.py", _rest_auth_code)
    init_code('user.py', _rest_user_handler_code)
    init_code('__init__.py', _rest_init_blueprint_code%("api","api"))


    # create test dir under dst path
    test_path=os.path.join(dst_path,'test')
    _mkdir_p(test_path)

    os.chdir(test_path)
    # create files under test/ dir
    init_code('__init__.py','''"the unittest package"''')
    init_code('test.py',_rest_test_code)

    # create utils/ dir under dst path
    utils_path=os.path.join(dst_path,'utils')
    _mkdir_p(utils_path)

    os.chdir(utils_path)
    # create files under utils/ dir
    init_code('__init__.py',_rest_util_init_code)
    init_code('pagenation.py',_util_pagenation_code)

    init_done_info()





# mana command set
cli.add_command(init)
cli.add_command(blueprint)
cli.add_command(startproject)
cli.add_command(admin)
cli.add_command(version)
cli.add_command(rest_startproject)


if __name__ == '__main__':
    cli()
