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
            options: "\nBooked\nCancelled\nCompleted\nChecked-In",
            reqd: 0
        }
    ],

    "formatter": function(value, row, column, data, default_formatter) {
        // Default formatting
        value = default_formatter(value, row, column, data);

        // Bold total row
        if(data.name === "TOTAL") {
            value = "<b style='color:green; font-size:14px;'>" + value + "</b>";
        }

        // Bold total_amount column in regular rows
        if(column.fieldname === "total_amount" && data.name !== "TOTAL") {
            value = "<b>" + value + "</b>";
        }

        return value;
    }
};
