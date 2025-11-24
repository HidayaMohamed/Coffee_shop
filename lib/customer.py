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
    
    