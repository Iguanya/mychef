import frappe

@frappe.whitelist()
def get_chefs():
    """Fetches all published chefs with relevant details"""
    return frappe.get_all(
        'Chefs', 
        filters={'published': 1}, 
        fields=['first_name', 'last_name', 'full_name', 'email_address'], 
        order_by='creation desc'
    )

def validate_permission():
    """Permission validation logic"""
    print("Permission function called")
    # Add your custom permission logic here
