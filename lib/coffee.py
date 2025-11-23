class Coffee:
    def __init__(self, name):
        self.name = name

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
        