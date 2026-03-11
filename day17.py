# class Human:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(self):
#         print(f"My name is {self.name} and age is: {self.age}")

# h1=Human("Suman",56)
# h1.greet()

# h2=Human("John",16)
# h2.greet()

# h3=Human()





# greet()

# def decorator(function1):
#     def wrapperFunc(*args):
#         print(*args)
#         print("-"*30)
#         function1("Shivam")
#         print("-"*30)
#     return wrapperFunc

# decorator1(greet)()
# decorator1(AddTwoNum)()

# @decorator
# def greet():
#     print("Hello good morning")

# @decorator
# def AddTwoNum():
#     num1=8
#     num3=3
#     print(num1+num3)

# greet()
# AddTwoNum()

# def decorator(function1):
#     def wrapperFunc(*args,**kwargs):
#         # print(kwargs)
#         print("-"*30)
#         function1(*args)
#         print("-"*30)
#     return wrapperFunc

# @decorator
# def greet(name):
#     print("Hello good morning",name)

# greet("Shivam",greeting="Hello")

class Human:

    def __init__(self,name,age):
        self._name=name
        self._age=age

    def greet(self):
        print(f"My name is {self.name} and age is: {self.age}")

    # def get_name(self):
    #     return self.name
    
    # def set_name(self,secondName):
    #     self.name=secondName

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self,secondName):
        self._name=secondName

h1=Human("John",78)

# h1.name=456789

# print(h1.get_name())
# h1.set_name("Gaurika")
# print(h1.get_name())

print(h1.name)

# h1.greet()