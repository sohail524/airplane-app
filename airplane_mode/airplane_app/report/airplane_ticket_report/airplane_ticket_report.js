frappe.query_reports["Airplane Ticket Report"] = {
    "filters": [
        {
            fieldname: "ticket_no",
            label: __("Ticket Number"),
            fieldtype: "Data",
            reqd: 0
        },
        {
            fieldname: "passenger",
            label: __("Passenger"),
            fieldtype: "Data",
            reqd: 0
        },
        {
            fieldname: "source_airport",
            label: __("Source Airport"),
            fieldtype: "Link",
            options: "Airport",
            reqd: 0
        },
        {
            fieldname: "destination_airport",
            label: __("Destination Airport"),
            fieldtype: "Link",
            options: "Airport",
            reqd: 0
        },
        {
            fieldname: "status",
            label: __("Status"),
            fieldtype: "Select",
            options: "Booked\nCancelled\nCompleted\nBooked\nChecked-In",
            reqd: 0
        }
    ]
};
