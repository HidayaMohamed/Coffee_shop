from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bobby")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Mocha")

c1.create_order(coffee1, 5.5)
c1.create_order(coffee2, 4.0)
c2.create_order(coffee1, 6.0)

print("Alice Coffees:", c1.coffees())
print("Latte Customers:", coffee1.customers())