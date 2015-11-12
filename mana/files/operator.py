# coding: utf-8

"""
	OS independent mkdir function
"""

import os


def mkdir(path):
	path = path.strip()
	path = path.rstrip("\\")

	is_path_exists = os.path.exists(path)

	if not is_path_exists:
		os.makedirs(path)
		print path + "create done !"
		return True
	else:
		print path + "already exists!"
		return False
