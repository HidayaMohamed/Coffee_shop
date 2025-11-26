# imports other classes
from .order import Order
from .coffee import Coffee

class Customer:
    # A class variable that stores all the customers.
    all = []
    # the class is initialized with name.
    def __init__(self, name):
        self.name = name
    #    Updated the class list all when a cusomer is instantiated.
        Customer.all.append(self)

    # Sets property for name and validates the anme is a string and between 1 - 15 characters. 
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

    # Returns alist of orders, this customer has ordered.
    def orders(self): 
        return [order for order in Order.all if order.customer is self]
    
    # Return ALL unique Coffee objects this customer has ordered.
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    # THis method creates an order for a cutomer.
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    # 
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

            # if a customer doesn't spend , sets spending to 0
            if customer not in spending:
                spending[customer] = 0

            spending[customer] += price

        # Find and return the customer who spent the most
        most_spending_customer = max(spending, key=spending.get)
        return most_spending_customer