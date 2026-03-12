
# class Car:
#     def __init__(self,name):
#         self.name=name

#     @property
#     def get_name(self):
#         return self.name
    
#     @get_name.setter
#     def set_name(self,secondName):
#         self.name=secondName

# c1=Car("Tesla")

# print(c1.name)

# c1.set_name="Yamaha"
# print(c1.get_name)

class Animal:
    def __init__(self,name):
        self.name=name

    def run(self):
        print(f"{self.name} is Running....")

a1=Animal("Horse")

# a1.run()
# Animal.run(a1)

# a1.run()

# b1=Animal("Goat")

# Animal.run(b1)
# b1.run()

a1.run()