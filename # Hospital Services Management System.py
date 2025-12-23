 # Hospital Services Management System
# Menu-driven Python Application

# ----------------- SERVICE CLASSES -----------------
class Service:
    def __init__(self, service_id, name, price):
        self.service_id = service_id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.service_id}\t{self.name}\tKES {self.price}")

class DiscountedService(Service):
    def __init__(self, service_id, name, price, discount):
        super().__init__(service_id, name, price)
        self.discount = discount

    def get_final_price(self):
        return self.price - (self.price * self.discount / 100)

# ----------- PAYMENT (INHERITANCE & POLYMORPHISM) -----------
class Payment:
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Payment of KES {amount} made in Cash.")

class MpesaPayment(Payment):
    def pay(self, amount):
        print(f"Payment of KES {amount} made via M-Pesa.")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of KES {amount} made using Card.")

# ----------------- DATA STRUCTURES -----------------
services = [
    Service(1, "General Consultation", 2000),
    DiscountedService(2, "Laboratory Test", 3000, 10),
    Service(3, "Pharmacy Services", 1500),
    DiscountedService(4, "Dental Checkup", 4000, 15),
    Service(5, "Physiotherapy", 2500)
]
records = []

# ----------------- FUNCTIONS -----------------
def add_record():
    record_id = len(records) + 1
    name = input("Enter patient name: ")
    records.append({"id": record_id, "name": name})
    print("Record added successfully.")

def view_records():
    if not records:
        print("No records available.")
    else:
        for record in records:
            print(record)

def search_record():
    rid = int(input("Enter record ID to search: "))
    for record in records:
        if record["id"] == rid:
            print(record)
            return
    print("Record not found.")

def update_record():
    rid = int(input("Enter record ID to update: "))
    for record in records:
        if record["id"] == rid:
            new_name = input("Enter new name: ")
            record["name"] = new_name
            print("Record updated successfully.")
            return
    print("Record not found.")

def show_services():
    print("\nID\tService\t\t\tPrice")
    for s in services:
        s.display()

def process_payment():
    show_services()
    sid = int(input("\nSelect service ID: "))

    selected = None
    for s in services:
        if s.service_id == sid:
            selected = s
            break

    if not selected:
        print("Invalid service selected.")
        return

    if isinstance(selected, DiscountedService):
        total = selected.get_final_price()
        print(f"Discount Applied: {selected.discount}%")
    else:
        total = selected.price

    print(f"Total Amount: KES {total}")
    print("\nPayment Methods:")
    print("1. Cash")
    print("2. M-Pesa")
    print("3. Card")

    choice = input("Choose payment method: ")

    if choice == "1":
        payment = CashPayment()
    elif choice == "2":
        payment = MpesaPayment()
    elif choice == "3":
        payment = CardPayment()
    else:
        print("Invalid payment option.")
        return

    payment.pay(total)

# ----------------- MAIN MENU -----------------
def main():
    while True:
        print("\n--- HOSPITAL MANAGEMENT SYSTEM ---")
        print("1. Add New Patient Record")
        print("2. View All Records")
        print("3. Search Record by ID")
        print("4. Update Record")
        print("5. View Services & Make Payment")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record()
        elif choice == "4":
            update_record()
        elif choice == "5":
            process_payment()
        elif choice == "6":
            print("Thank you for using the system.")
            break
        