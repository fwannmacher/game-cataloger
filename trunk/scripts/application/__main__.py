"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import sys
from .. import util
from .. import gui
from .. import sql

if __name__ == "__main__":
	util.ApplicationManager.set_path(sys.argv[1])
	sql.util.ConnectionManager.setup(sys.argv[1], "database.sqlite")
	sql.util.DatabaseManager.setup_database()
	application_window = gui.ApplicationWindow()
	util.ApplicationManager.set_application_window(application_window)

	application_window.run()