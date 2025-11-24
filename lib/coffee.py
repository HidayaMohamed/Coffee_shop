from .order import Order

class Coffee:
    all =[]
    def __init__(self, name):
        self.name = name

        Coffee.all.append(self)
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
        
    def orders(self):
        # Return all Order objects that include THIS coffee.
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        # Return UNIQUE Customer objects who ordered this coffee
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        return sum(order.price for order in self.orders) / len(self.orders)