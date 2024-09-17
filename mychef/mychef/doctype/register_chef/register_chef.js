// Copyright (c) 2024, George Mwangi and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Register Chef", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Register Chef', {
    is_client: function(frm) {
        if (frm.doc.is_client) {
            frm.set_active_tab('Tab 2');  // Switch to second tab if client
        } else {
            frm.set_active_tab('Details');  // Default back to first tab if not client
        }
    }
});
