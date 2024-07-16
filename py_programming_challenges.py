# Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops 
# by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
def open_new_ticket(ticket_id, customer, issue):
    if ticket_id in service_tickets:
        print(f"Ticket {ticket_id} already exists.")
    else:
        service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket {ticket_id} opened for {customer}.")

def update_ticket_status(ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = status
        print(f"Ticket {ticket_id} status updated to {status}.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(status_filter=None):
    if status_filter:
        filtered_tickets = {k: v for k, v in service_tickets.items() if v["Status"] == status_filter}
        if filtered_tickets:
            for ticket_id, details in filtered_tickets.items():
                print(f"{ticket_id}: {details}")
        else:
            print(f"No tickets found with status {status_filter}.")
    else:
        for ticket_id, details in service_tickets.items():
            print(f"{ticket_id}: {details}")

open_new_ticket("Ticket003", "Charlie", "Account locked")
update_ticket_status("Ticket001", "closed")
display_tickets()
display_tickets("open")
display_tickets("closed")