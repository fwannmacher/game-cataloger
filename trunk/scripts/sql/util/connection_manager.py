"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import sqlite3
import os

class ConnectionManager:
	_database = None

	@classmethod
	def setup(cls, path, database):
		cls._database = os.path.join(path, database)

	@classmethod
	def get_connection(cls):
		connection = sqlite3.connect(cls._database)
		connection.row_factory = sqlite3.Row

		return connection