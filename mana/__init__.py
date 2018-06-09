import sys,os
base_dir=os.path.abspath(os.path.dirname(__file__))
print(base_dir)
sys.path.append(base_dir)
#
from mana import operators
from mana import templates