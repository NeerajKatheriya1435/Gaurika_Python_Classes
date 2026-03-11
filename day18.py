class Human:

    def __init__(self,name,age):
        self._name=name
        self._age=age

    def greet(self):
        print(f"My name is {self._name} and age is: {self._age}")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value): # Setter
        if len(value) > 5:
            self._name = value
        else:
            print("Invalid name")

# h1=Human("Rohan",89)
# print(h1._name)
# h1.greet()
# h1.name="Geeta Kumari"
# print(h1.name)
# h1.greet()