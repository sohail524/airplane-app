# Copyright (c) 2025, sohail and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe.utils import flt

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    totals = get_totals(data)

    if totals:
        data.append(totals)

    return columns, data


def get_columns():
    return [
        {"label": "Ticket No", "fieldname": "name", "fieldtype": "Link", "options": "Airplane Ticket", "width": 120},
        {"label": "Passenger", "fieldname": "passenger", "fieldtype": "Data", "width": 150},
        {"label": "Source", "fieldname": "source_airport", "fieldtype": "Data", "width": 120},
        {"label": "Destination", "fieldname": "destination_airport", "fieldtype": "Data", "width": 120},
        {"label": "Departure Date", "fieldname": "departure_date", "fieldtype": "Date", "width": 120},
        {"label": "Seat", "fieldname": "seat", "fieldtype": "Data", "width": 80},
        {"label": "Flight Price", "fieldname": "flight_price", "fieldtype": "Currency", "width": 120},
        {"label": "Add-ons Total", "fieldname": "addons_total", "fieldtype": "Currency", "width": 120},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 130},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]


def get_data(filters):
    conditions = "1=1"

    if filters.get("passenger"):
        conditions += f" AND at.passenger LIKE '%{filters.get('passenger')}%'"

    if filters.get("status"):
        conditions += f" AND at.status = '{filters.get('status')}'"

    if filters.get("from_date"):
        conditions += f" AND at.departure_date >= '{filters.get('from_date')}'"

    if filters.get("to_date"):
        conditions += f" AND at.departure_date <= '{filters.get('to_date')}'"

    records = frappe.db.sql(f"""
        SELECT
            at.name,
            at.passenger,
            at.source_airport,
            at.destination_airport,
            at.departure_date,
            at.seat,
            at.flight_price,
            at.total_amount,
            at.status,
            (
                SELECT COALESCE(SUM(amount), 0)
                FROM `tabAirplane Ticket Add-on Item`
                WHERE parent = at.name
            ) AS addons_total
        FROM `tabAirplane Ticket` at
        WHERE {conditions}
        ORDER BY at.departure_date ASC
    """, as_dict=True)

    return records


def get_totals(data):
    if not data:
        return None

    total_flight_price = sum(flt(d.flight_price) for d in data)
    total_addons = sum(flt(d.addons_total) for d in data)
    total_amount = sum(flt(d.total_amount) for d in data)

    return {
        "name": "TOTAL",
        "flight_price": total_flight_price,
        "addons_total": total_addons,
        "total_amount": total_amount,
        "__bold": 1
    }
