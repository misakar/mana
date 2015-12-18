# coding: utf-8

"""
    init_code.py
    ~~~~~~~~~~~~

        create and write init code in a file
"""

def init_code(filename, init_code):
    """create and write init code in a file"""
    with open(filename, 'w+') as f:
        f.write(init_code)
