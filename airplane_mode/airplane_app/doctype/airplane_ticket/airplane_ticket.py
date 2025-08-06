# Copyright (c) 2025, sohail and contributors
# For license information, please see license.txt
import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):

    def before_insert(self):
        self.check_flight_capacity()

        # assign seat only if not already set
        if not self.seat:
            row = random.randint(1, 150)
            seat_letter = random.choice(["A", "B", "C", "D", "E"])
            self.seat = f"{row}{seat_letter}"

    def validate(self):
        self.calculate_total_amount()

    def calculate_total_amount(self):
        total_add_ons = 0.0
        for item in self.add_ons:
            total_add_ons += item.amount or 0.0

        self.total_amount = (self.flight_price or 0.0) + total_add_ons

    def check_flight_capacity(self):
        if not self.flight:
            return

        # Get the airplane from the flight
        airplane = frappe.db.get_value("Airplane Flight", self.flight, "airplane")

        if not airplane:
            return

        # Get the capacity of the airplane
        capacity = frappe.db.get_value("Airplane", airplane, "capacity") or 0

        # Count how many tickets already exist for this flight
        booked_seats = frappe.db.count("Airplane Ticket", {
            "flight": self.flight,
            "docstatus": 1  # count only submitted tickets
        })

        if booked_seats >= capacity:
            frappe.throw(f"Cannot book ticket. Flight is fully booked with {capacity} seats.")

