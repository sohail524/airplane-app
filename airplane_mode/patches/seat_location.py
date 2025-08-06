import frappe
import random
import string

def execute():
    # Get all Airplane Tickets where 'seat' is empty or NULL
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["is", "not set"]}, fields=["name"])
    
    for ticket in tickets:
        random_number = random.randint(1, 99)
        random_letter = random.choice(["A", "B", "C", "D", "E"])
        seat = f"{random_number}{random_letter}"
        
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)
    
    frappe.db.commit()
