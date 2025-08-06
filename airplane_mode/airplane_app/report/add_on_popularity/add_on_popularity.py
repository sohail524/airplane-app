# Copyright (c) 2025, sohail and contributors
# For license information, please see license.txt
import frappe
from frappe.query_builder import DocType
from pypika import functions as fn, Order

def execute(filters=None):
    AddOn = DocType("Airplane Ticket Add On")

    data = (
        frappe.qb.from_(AddOn)
        .select(AddOn.add_on, fn.Count("*").as_("sold_count"))
        .groupby(AddOn.add_on)
        .orderby(fn.Count("*"), order=Order.desc)  # ✅ correct usage here
    ).run(as_dict=True)

    columns = [
        {"label": "Add-On", "fieldname": "add_on", "fieldtype": "Link", "options": "Add On"},
        {"label": "Sold Count", "fieldname": "sold_count", "fieldtype": "Int"}
    ]

    return columns, data
