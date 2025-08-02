// Copyright (c) 2025, sohail and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Flight Passenger", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Flight Passenger', {
    first_name: function(frm) {
        update_full_name(frm);
    },
    last_name: function(frm) {
        update_full_name(frm);
    },
    refresh: function(frm) {
        update_full_name(frm);
    }
});

function update_full_name(frm) {
    const fullName = `${frm.doc.first_name || ""} ${frm.doc.last_name || ""}`.trim();
    frm.set_value('full_name', fullName);
}