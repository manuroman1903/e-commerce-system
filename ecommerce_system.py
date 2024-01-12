# ecommerce_system.py
from customer import Customer
from product import Product
from order import Order
from shopping_cart import ShoppingCart

# Create customers
customer1 = Customer("John Doe", "john@example.com")
customer2 = Customer("Jane Doe", "jane@example.com")

# Create products
product1 = Product("Laptop", 1200.0)
product2 = Product("Headphones", 99.99)

# Create shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add items to shopping carts
cart1.add_item(product1)
cart2.add_item(product2)

# Create orders
order1 = Order(1, cart1.items)
order2 = Order(2, cart2.items)

# Add orders to customers
customer1.add_order(order1)
customer2.add_order(order2)

# Display customer information
print("Customer Information:")
customer1.display_customer_info()
print()
customer2.display_customer_info()
