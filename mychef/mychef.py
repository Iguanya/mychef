import frappe

def get_context(context):
    """Pass chefs data to the template context"""
    context.chefs = frappe.get_all('Chefs', filters={'published': 1}, fields=['full_name', 'email_address'])
