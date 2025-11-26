# imports order class
from .order import Order

class Coffee:
    # class variable
    all =[]
    # initialized with name
    def __init__(self, name):
        self.name = name
        # when an instance is called, the all is append.
        Coffee.all.append(self)

    #sets property for coffee name to be a string and atleast 3chars.
    @property 
    def name(self):
        return self._name 
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Coffee name must be a string.")
        if not len(value)< 3:
            raise Exception("Coffee name must be atleast 3 characters long.")
        self._name = value


     # Return all Order objects that include This coffee.
    def orders(self): 
        return [order for order in Order.all if order.coffee is self]

    # Return UNIQUE Customer objects who ordered this coffee
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    # Returns total number of orders for this coffee.  
    def num_orders(self):
        return len(self.orders)
    
    # Returns the average price for this coffee.
    def average_price(self):
        return sum(order.price for order in self.orders) / len(self.orders)