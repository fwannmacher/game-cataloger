"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

from .. import sql
from .. import util
from update_database_window import UpdateDatabaseWindow

class UpdateDatabaseHandler:
	@staticmethod
	def on_update_database_button_click(button, tree_view, toggle_index, wrapper_index):
		model = tree_view.get_model()
		update_database_window = UpdateDatabaseWindow()
		folder_counter = 0
		manufacturers, folder_total = UpdateDatabaseHandler.__handle_manufacturers(model.iter_children(model.get_iter("0")), model, toggle_index, wrapper_index)

		for manufacturer in manufacturers:
			for device in manufacturer.get_devices():
				for folder in device.get_folders():
					folder_counter += 1
					sql.wrapper.Game.destroy_all_where("folder_id = {0} AND file_name NOT {1}".format(folder.get_id(), UpdateDatabaseHandler.__build_in_statement(folder.get_games())))
					games_to_save = []

					for game in folder.get_games():
						if not sql.wrapper.Game.find_by_file_name(game.get_file_name()).get_id():
							games_to_save.append(game)

					sql.wrapper.Game.save_all(games_to_save, folder, "folder_id")
					update_database_window.on_progress_update(folder_counter, folder_total)

		update_database_window.destroy()

	@staticmethod
	def __handle_manufacturers(iter, model, toggle_index, wrapper_index):
		manufacturers = []
		folder_counter = 0

		while iter is not None:
			if model[iter][toggle_index]:
				manufacturer = sql.wrapper.Manufacturer.find_by_id(model[iter][wrapper_index])
				devices, counter = UpdateDatabaseHandler.__handle_devices(model.iter_children(iter), model, toggle_index, wrapper_index, manufacturer)
				manufacturer.add_devices(devices)
				manufacturers.append(manufacturer)
				folder_counter += counter

			iter = model.iter_next(iter)

		return manufacturers, folder_counter

	@staticmethod
	def __handle_devices(iter, model, toggle_index, wrapper_index, manufacturer):
		devices = []
		folder_counter = 0

		while iter is not None:
			if model[iter][toggle_index]:
				device = sql.wrapper.Device.find_by_id(model[iter][wrapper_index])
				folders = UpdateDatabaseHandler.__handle_folders(model.iter_children(iter), model, toggle_index, wrapper_index, device)
				device.add_folders(folders)
				devices.append(device)
				folder_counter += len(folders)

			iter = model.iter_next(iter)

		return devices, folder_counter
	
	@staticmethod
	def __handle_folders(iter, model, toggle_index, wrapper_index, device):
		folders = []

		while iter is not None:
			if model[iter][toggle_index]:
				folder = sql.wrapper.Folder.find_by_id(model[iter][wrapper_index])
				folder.add_games(util.GameFinder.find(folder))
				folders.append(folder)

			iter = model.iter_next(iter)

		return folders

	@staticmethod
	def __build_in_statement(games):
		values = ""

		for game in games:
			if len(values) > 0:
				values += ","

			values += "'{0}'".format(game.get_file_name().replace("'", "''"))

		return "IN ({0})".format(values)
