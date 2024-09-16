import frappe

def get_context(context):
    context.chefs = frappe.get_all('Chefs', fields=['first_name', 'last_name', 'full_name', 'email_address', 'phone', 'published', 'chefs'])
