import frappe

@frappe.whitelist()
def get_chefs():
    return frappe.db.get_all('Chefs', fields=['first_name', 'last_name', 'email_address'])

def validate_permission():
    print("Permission function called")
    # your permission logic here
