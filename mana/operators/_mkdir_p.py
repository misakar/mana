# coding: utf-8

"""
_mkdir_p.py
~~~~~~~~~~~

Usage:

    _mkdir_p(abspath):
        create the abspath
        except the abspath exist

Param:

    abspath: the absolutly path you want to be created

"""

import os, errno


def _mkdir_p(abspath):
    """
    Usage:
        create the abspath
        except the abspath exist

    Param:
        abspath: the absolutly path you want to be created
    """
    try:
        os.makedirs(abspath)
    except OSError as e:
        if (e.errno == errno.EEXIST) and (os.path.isdir(abspath)):
            pass
        else: raise
