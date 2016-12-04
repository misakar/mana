# coding: utf-8

"""
[unittest]
test_mana for test mana
"""

import unittest
# test create
from mana.mana import create_templates_static_files, create_blueprint
# test command
from mana.mana import init, startproject, admin, version, blueprint
from setup import version


class ManaTestCase(unittest.TestCase):
    """mana test cases"""

    def test_command_init(self):
        # test command init
        pass

    def test_command_startproject(self):
        pass

    def test_command_admin(self):
        pass

    def test_command_version(self):
        # test mana version
        test_mana_version = "mana version: %s \/" % version
        mana_version = eval("mana version")
        self.assertTrue(mana_version=test_mana_version)

    def test_command_blueprint(self):
        pass

if __name__ == "__main__":
    unittest.main()
