# Copyright (c) 2024, George Mwangi and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Chefs(WebsiteGenerator):
	def before_save(self):
		self.full_name= f'{self.first_name} {self.last_name or ""}'
