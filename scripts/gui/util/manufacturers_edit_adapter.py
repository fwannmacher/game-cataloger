"""
Generated by <Python Project Utils>
Visit the project in http://code.google.com/p/python-project-utils/
"""

from ... import sql
from edit_adapter import IEditAdapter

class ManufacturersEditAdapter(IEditAdapter):
	def get_items_parameters(self):
		return {"Name" : "text"}

	def get_items_list(self):
		list = []

		for item in sql.wrapper.Manufacturer.find_all():
			list.append([item.get_id(), str(item.get_name())])

		return list

	def items_have_parent(self):
		return False

	def get_item_values(self, id):
		return {"Name" : sql.wrapper.Manufacturer.find_by_id(id).get_name()}

	def save_item_values(self, id, parameters):
		item = sql.wrapper.Manufacturer.find_by_id(id) if id != None else sql.wrapper.Manufacturer()
		item.set_name(parameters["Name"])
		item.save()
