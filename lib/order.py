from .customer import Customer
from .coffee import Coffee


class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price


        Order.all.append(self)

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
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def cusomer(self, value):
        if not isinstance(value, Customer):
            raise Exception("customer must be a Customer instanace")
        self._customer = value

    @property
    def coffee(self):
        return self._coffe
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise Exception("coffee must be a Coffee instance")
        self._coffee = value
