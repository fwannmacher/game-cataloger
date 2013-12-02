"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

from connection_manager import *

class DatabaseManager:
	@staticmethod
	def setup_database():
		connection = ConnectionManager.get_connection()

		with connection:
			DatabaseManager.__create_manufacturers_table(connection)
			DatabaseManager.__create_devices_table(connection)
			DatabaseManager.__create_folders_table(connection)
			DatabaseManager.__create_games_table(connection)

		connection.close()

	@staticmethod
	def __create_manufacturers_table(connection):
		connection.execute("""
					CREATE TABLE IF NOT EXISTS manufacturers (
						id INTEGER PRIMARY KEY,
						name TEXT
					);
			""")

	@staticmethod
	def __create_devices_table(connection):
		connection.execute("""
					CREATE TABLE IF NOT EXISTS devices (
						id INTEGER PRIMARY KEY,
						name TEXT,
						manufacturer_id INTEGER,
						FOREIGN KEY(manufacturer_id)
							REFERENCES manufacturers(id)
							ON DELETE CASCADE
					);
			""")

	@staticmethod
	def __create_folders_table(connection):
		connection.execute("""
					CREATE TABLE IF NOT EXISTS folders (
						id INTEGER PRIMARY KEY,
						alias TEXT,
						path TEXT,
						is_compressed BOOL,
						compression_engine TEXT,
						device_id INTEGER,
						FOREIGN KEY(device_id)
							REFERENCES devices(id)
							ON DELETE CASCADE
					);
			""")

	@staticmethod
	def __create_games_table(connection):
		connection.execute("""
					CREATE TABLE IF NOT EXISTS games (
						id INTEGER PRIMARY KEY,
						name TEXT,
						media_id TEXT,
						file_name TEXT,
						folder_id INTEGER,
						FOREIGN KEY(folder_id)
							REFERENCES folders(id)
							ON DELETE CASCADE
					);
			""")