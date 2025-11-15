// Copyright (c) 2025, sohail and contributors
// For license information, please see license.txt

frappe.query_reports["Airplane Ticket Report"] = {
    formatter: function(value, row, column, data, default_formatter) {
        let formatted = default_formatter(value, row, column, data);
        if (data && data.name === "TOTAL") {
            formatted = `<strong>${formatted}</strong>`;
        }
        return formatted;
    },

    filters: [
        {
            "fieldname": "passenger",
            "label": __("Passenger Name"),
            "fieldtype": "Data",
            "width": 150
        },
        {
            "fieldname": "status",
            "label": __("Status"),
            "fieldtype": "Select",
            "options": ["", "Booked", "Cancelled", "Completed"],
            "width": 120
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date"
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date"
        }
    ]
};
