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

@frappe.whitelist()
def create_user(doc, method):
    if doc.email_address:
        # Check if the email already exists
        if frappe.db.exists("User", {"email": doc.email_address}):
            frappe.throw(f"Email {doc.email_address} is already registered.")
        else:
            # Create user if the email does not exist
            user = frappe.get_doc({
                "doctype": "User",
                "email": doc.email_address,
                "first_name": doc.first_name,
                "last_name": doc.last_name,
                "enabled": 1,
                "user_type": "Website User",
                "send_welcome_email": 1,
                "new_password": doc.password,  # Set the password
                "roles": [{"role": "Customer"}]  # or assign "Chef" based on a field
            })
            user.insert(ignore_permissions=True)
            frappe.msgprint(f"User {doc.email_address} created successfully.")



def validate_permission():
    """Permission validation logic"""
    print("Permission function called")
    # Add your custom permission logic here
