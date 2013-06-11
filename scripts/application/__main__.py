"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

import sys
from .. import gui
from .. import sql

if __name__ == "__main__":
	sql.util.ConnectionManager.setup(sys.argv[1], "database.sqlite")
	gui.CoverViewManager.set_path(sys.argv[1])
	application_window = gui.ApplicationWindow()
	gui.ApplicationWindowManager.set_application_window(application_window)

	application_window.run()
