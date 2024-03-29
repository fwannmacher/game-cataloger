"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import pygtk
pygtk.require('2.0')
import gtk
from search_box import SearchBox
from menu_bar import MenuBar
from icon_scrolled_window import IconScrolledWindow

class ApplicationWindow(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self)

		self.set_position(gtk.WIN_POS_CENTER)
		self.maximize()
		self.connect("destroy", gtk.main_quit)
		self.set_title("Game Cataloger")

		accel_group = gtk.AccelGroup()
		self.add_accel_group(accel_group)

		window_box = gtk.VBox(False, 2)

		main_paned = gtk.HPaned()
		main_paned.pack1(SearchBox())
		main_paned.pack2(IconScrolledWindow())
		
		window_paned = gtk.VPaned()
		window_paned.pack1(main_paned, True)
		window_paned.pack2(gtk.VBox(), False)

		window_box.pack_start(MenuBar(accel_group, self), False)
		window_box.pack_start(window_paned, True)
		self.add(window_box)
		self.show_all()

	def run(self):
		gtk.main()
