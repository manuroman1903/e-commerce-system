# customer.py
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def display_customer_info(self):
        print(f"Customer Name: {self.name}, Email: {self.email}")
        print("Orders:")
        for order in self.orders:
            order.display_order_info()
            print()
