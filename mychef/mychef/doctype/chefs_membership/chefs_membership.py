# Copyright (c) 2024, George Mwangi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus


class ChefsMembership(Document):
	def before_submit(self):
		exists = frappe.db.exists(
			"Chefs Membership",
			{
			"members": self.members,
			"docstatus": DocStatus.submitted(),
			"to_date": (">", self.from_date)
			},
		)

		if exists:
			frappe.throw("There is an active Membership for this member")
