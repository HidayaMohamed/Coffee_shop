class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price 
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise Exception("Price must be a float.")
        if not(1.0 <= value <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")
        self._price = value
    