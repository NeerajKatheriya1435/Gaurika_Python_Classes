
# class Car:
#     name="Tesla"

#     def __init__(self,engine,speed):
#         self.engine=engine
#         self.speed=speed

#     def details(self):
#         print(f"My engine is: {self.engine} and speed is: {self.speed}")
    
#     @classmethod
#     def design(cls,color):
#         cls.name="Hero"
#         print(f"My car name is: {cls.name} and color is: {color}")


# c1=Car("125CC",200)

# c1.details()
# c1.design("Blue")

# Car.name="Yamaha"

# Car.design("Blue")




# str1="hello"
# print(str1.index("l",3))

# for i in str1:
#     print(str1.index(i))

# class Person:
#     def __init__(self, name, age,adhar):
#         self.name = name
#         self.age = age
#         self.adhar = adhar

#     @classmethod
#     def from_string(cls, data_str):
#         name, age,adhar = data_str.split(' ')
#         return cls(name, int(age),int(adhar))

# p1 = Person("Neeraj", 23)

# Creating object using alternative constructor

# p2 = Person.from_string("Neeraj 23 1234567890")

# print(p1.name, p1.age) # Neeraj 23

# print(p2.name, p2.age, p2.adhar) # Neeraj 23



# class Bike:
#     def __init__(self,name):
#         print("Hello Bike Constructor")
#         self.name=name

#     def details(self):
#         print(f"My engine is {self.name} ")


# class Car(Bike):
#     def __init__(self, name,color):
#         super().__init__(name)
#         print("Hello Constructor")
#         self.color=color

#     def det(self):
#         print(f"My engine is Car1 ")

#     def details(self):
#         # super().details()
#         print(f"My Car Color is {self.color}")


# c1=Bike()
# c1.details()

# c2=Car()
# c2.details()

c2=Car("Tesla","Black")
c2.details()