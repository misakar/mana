# coding: utf-8

"""
	test_mana.py
	~~~~~~~~~~~~

		测试mana的安装
"""

import click
from click.testing import CliRunner


def test_mana():
	@click.command()
	@click.argument('init')
	def hello(init):
		click.echo("")
