"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

class ApplicationManager:
	_path = None
	_application_window = None

	@staticmethod
	def get_path():
		return ApplicationManager._path

	@staticmethod
	def get_application_window():
		return ApplicationManager._application_window

	@staticmethod
	def set_path(path):
		ApplicationManager._path = path

	@staticmethod
	def set_application_window(application_window):
		ApplicationManager._application_window = application_window
