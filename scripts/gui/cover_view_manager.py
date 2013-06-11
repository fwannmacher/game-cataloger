"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import pygtk
pygtk.require('2.0')
import gtk
from notifier import Notifier
from cover_loader import CoverLoader

class CoverViewManager:
	_path = None
	_icon_view = None

	@staticmethod
	def update_view(manufacturers):
		list_store = gtk.ListStore(gtk.gdk.Pixbuf, str, str)
		list_store.set_sort_column_id(1, gtk.SORT_ASCENDING)
		game_count = 0

		for manufacturer in manufacturers:
			for device in manufacturer.get_devices():
				for folder in device.get_folders():
					for game in folder.get_games():
						list_store.append([CoverLoader.load(CoverViewManager._path, manufacturer, device, game, 184, 256), game.get_name(), folder.get_path()])
						game_count += 1

		CoverViewManager._icon_view.set_model(list_store)
		Notifier.create_info_notification("Search Result", "{0} game{1} found".format(game_count, "" if game_count == 1 else "s"))

	@staticmethod
	def set_path(path):
		CoverViewManager._path = path

	@staticmethod
	def set_icon_view(icon_view):
		CoverViewManager._icon_view = icon_view