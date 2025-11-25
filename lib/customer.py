from .order import Order
from .coffee import Coffee

class Customer:
    all = []
    def __init__(self, name):
        self.name = name

        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise Exception("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        # Returns alist of orders, this customer has ordered. 
        return [order for order in Order.all if order.customer is self]
    def coffees(self):
        # Return ALL unique Coffee objects this customer has ordered.
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    

    @classmethod
    def most_aficionado(cls, coffee):
        # Make sure the argument is a Coffee object
        if not isinstance(coffee, Coffee):
            raise Exception("Must pass a Coffee instance.")

        # List of orders that match the given coffee
        coffee_orders = []
        for order in Order.all:
            if order.coffee is coffee:
                coffee_orders.append(order)

        # If nobody ordered this coffee, return None
        if len(coffee_orders) == 0:
            return None

        # Dictionary to track how much each customer spent
        spending = {}
        for order in coffee_orders:
            customer = order.customer
            price = order.price

            if customer not in spending:
                spending[customer] = 0

            spending[customer] += price

        # Find and return the customer who spent the most
        most_spending_customer = max(spending, key=spending.get)
        return most_spending_customer