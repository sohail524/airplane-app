# Copyright (c) 2025, sohail and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):

    def before_insert(self):
        # Random seat assignment (e.g. 12B, 44D)
        row = random.randint(1, 150)
        seat_letter = random.choice(["A", "B", "C", "D", "E"])
        self.seat = f"{row}{seat_letter}"

    def validate(self):
        self.calculate_total_amount()

    def calculate_total_amount(self):
        total_add_ons = 0.0
        

		

        # Sum all add-on item amounts
        for item in self.add_ons:
            total_add_ons += item.amount or 0.0

        # Add to base flight price
        self.total_amount = (self.flight_price or 0.0) + total_add_ons
