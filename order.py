# order.py
class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def display_order_info(self):
        print(f"Order ID: {self.order_id}, Total: ${self.calculate_total()}")
        print("Products:")
        for product in self.products:
            print(f"- {product.name}: ${product.price}")
