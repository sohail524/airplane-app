# airplane_ticket_report.py
import frappe
from frappe.utils import flt

def execute(filters=None):
    filters = filters or {}

    columns = get_columns()
    data = get_data(filters)

    totals = get_totals(data)
    if totals:
        data.append(totals)

    return columns, data


def get_columns():
    return [
        {"label": "Ticket ID", "fieldname": "name", "fieldtype": "Link", "options": "Airplane Ticket", "width": 120},
        {"label": "Passenger", "fieldname": "passenger", "fieldtype": "Data", "width": 150},
        {"label": "Source Airport", "fieldname": "source_airport", "fieldtype": "Link", "options": "Airport", "width": 150},
        {"label": "Destination Airport", "fieldname": "destination_airport", "fieldtype": "Link", "options": "Airport", "width": 150},
        {"label": "Departure Date", "fieldname": "departure_date", "fieldtype": "Date", "width": 120},
        {"label": "Seat", "fieldname": "seat", "fieldtype": "Data", "width": 80},
        {"label": "Flight Price", "fieldname": "flight_price", "fieldtype": "Currency", "width": 120},
        {"label": "Add-ons Amount", "fieldname": "addons_amount", "fieldtype": "Currency", "width": 120},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 120},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100}
    ]


def build_conditions(filters):
    conditions = []
    if filters.get("ticket_id"):
        conditions.append("t.name = %(ticket_id)s")
    if filters.get("passenger"):
        conditions.append("t.passenger = %(passenger)s")

    return " AND " + " AND ".join(conditions) if conditions else ""


def get_data(filters):
    conditions = build_conditions(filters)

    tickets = frappe.db.sql(f"""
        SELECT 
            t.name,
            t.passenger,
            t.source_airport,
            t.destination_airport,
            t.departure_date,
            t.seat,
            t.flight_price,
            t.total_amount,
            t.status
        FROM `tabAirplane Ticket` t
        WHERE t.docstatus < 2 {conditions}
        ORDER BY t.departure_date ASC
    """, filters, as_dict=True)

    # Add-ons calculation
    for ticket in tickets:
        addons_amount = frappe.db.get_value(
            "Airplane Ticket Add-on Item",
            {"parent": ticket.name, "parentfield": "add_ons"},
            "SUM(amount)"
        ) or 0

        ticket["addons_amount"] = flt(addons_amount)
        ticket["total_amount"] = flt(ticket.get("flight_price")) + flt(ticket["addons_amount"])

    return tickets


def get_totals(data):
    if not data:
        return None

    total_flight = sum(flt(row.get("flight_price")) for row in data)
    total_addons = sum(flt(row.get("addons_amount")) for row in data)
    total_amount = sum(flt(row.get("total_amount")) for row in data)

    return {
        "name": "TOTAL",
        "flight_price": total_flight,
        "addons_amount": total_addons,
        "total_amount": total_amount
    }

    return tickets

def get_totals(data):
    if not data:
        return None

    total_amount = sum(flt(d.total_amount) for d in data)
    total_flight_price = sum(flt(d.flight_price) for d in data)
    total_addons = sum(flt(d.addons_amount) for d in data)

    return {
        "name": "TOTAL",
        "passenger": "",
        "source_airport": "",
        "destination_airport": "",
        "departure_date": "",
        "seat": "",
        "flight_price": total_flight_price,
        "addons_amount": total_addons,
        "total_amount": total_amount,
        "status": ""
    }
