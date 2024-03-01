#The S in SOLID is satisfied in this program by having a class being responsible for one thing 
class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address
        print("Order details stored successfully")

class OrderCostCalculator:
    def calculate_total_cost(self, items):
        total_cost = 100
        print("Total order cost calculated:", total_cost)

class OrderValidator:
    def validate_order(self, items, shipping_address):
        if items and shipping_address:
            print("Order data validated successfully")
        else:
            print("Order data validation failed")

class EmailSender:
    def send_confirmation_email(self, customer_email):
        print("Order confirmation email sent to", customer_email)

class InventoryUpdater:
    def update_inventory(self, items):
        print("Inventory levels updated after order processing")

def main():
    customer_info = {"name": "John Doe", "email": "johndoe@example.com"}
    items = ["Item1", "Item2"]
    shipping_address = "123 Main St, City, Country"

    order_details = OrderDetails(customer_info, items, shipping_address)
    order_cost_calculator = OrderCostCalculator()
    order_validator = OrderValidator()
    email_sender = EmailSender()
    inventory_updater = InventoryUpdater()

    order_validator.validate_order(items, shipping_address)
    order_cost_calculator.calculate_total_cost(items)
    email_sender.send_confirmation_email(customer_info['email'])
    inventory_updater.update_inventory(items)

if __name__ == "__main__":
    main()
