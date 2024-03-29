"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

from ... import sql
from edit_adapter import IEditAdapter
from devices_edit_adapter import DevicesEditAdapter

class FoldersEditAdapter(IEditAdapter):
	def __init__(self):
		self._parent_adapter = DevicesEditAdapter()

	def get_items_parameters(self):
		return {"Alias" : "text", "Path" : "text"}

	def get_items_list(self):
		list = []

		for item in sql.wrapper.Folder.find_all():
			list.append([item.get_id(), str(item.get_alias()), str(item.get_path())])

		return list

	def get_items_list_by_parent(self, id):
		list = []

		for item in sql.wrapper.Folder.find_all_by_foreign_key("device_id", sql.wrapper.Device.find_by_id(id)):
			list.append([item.get_id(), str(item.get_alias()), str(item.get_path())])

		return list

	def items_have_parent(self):
		return True

	def get_parent_type_name(self):
		return "Device"

	def get_items_parent_list(self):
		return self._parent_adapter.get_items_list()

	def get_item_parent(self, id):
		item = sql.wrapper.Folder.find_by_id(id)

		return self._parent_adapter.get_item_values(item.get_parent().get_id())

	def get_items_parent_list(self):
		list = []

		for item in sql.wrapper.Device.find_all():
			list.append([item.get_id(), str(item.get_name())])

		return list

	def get_item_values(self, id):
		item = sql.wrapper.Folder.find_by_id(id)
		return {"id" : id, "Alias" : item.get_alias(), "Path" : item.get_path()}

	def save_item_values(self, id, parameters):
		item = sql.wrapper.Folder.find_by_id(id) if id else sql.wrapper.Folder()
		item.set_alias(parameters["Alias"])
		item.set_path(parameters["Path"])
		item.save(sql.wrapper.Device.find_by_id(parameters[self.get_parent_type_name()]), "device_id")

		return item
