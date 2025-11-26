# imports other classes
from .customer import Customer
from .coffee import Coffee


class Order:
    # creates a class variable to store all instnaces
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        # everytime this class is instantiated, it is appended to the class list.
        Order.all.append(self)

    # sets property and setter validations for price.
    @property
    def price(self):
        return self._price 
    
    # validates price to be a float, and between 1.0 and 10.0.
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise Exception("Price must be a float.")
        if not(1.0 <= value <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")
        self._price = value

    # sets property for customer 
    @property
    def customer(self):
        return self._customer
    
    # validates customer to be a Customer instance
    @customer.setter
    def cusomer(self, value):
        if not isinstance(value, Customer):
            raise Exception("customer must be a Customer instanace")
        self._customer = value
    
    
    # sets property for coffee
    @property
    def coffee(self):
        return self._coffe
    
    # Validates coffee must be a Coffee instance.
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise Exception("coffee must be a Coffee instance")
        self._coffee = value
