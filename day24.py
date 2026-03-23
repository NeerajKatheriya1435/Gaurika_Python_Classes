class Person:
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_string(cls, data_str):
        name, age, salary = data_str.split('-')
        return cls(name, int(age),int(salary))
    
# Creating object normally

# str1="Neeraj-34-20000"

# str2=str1.split("-")

# print(str1)
# p1 = Person(str2[0],str2[1],str2[2])

# print(p1.name)
# print(p1.age)
# print(p1.salary)

# Creating object using alternative constructor
# p2 = Person.from_string("Neeraj-23-20000")

# print(p1.name, p1.age) # Neeraj 23
# print(p2.name, p2.age,p2.salary) # Neeraj 23

# print(dir(Person))
# print(p2.__dict__)

# class Person:

#     def __init__(self,name,age):
#         print("Hello Contrutor")
#         self.name=name
#         self.age=age

#     def func1(self):
#         print("hello Gaurika")

# class Gaurika(Person):

#     def __init__(self, name, age,lang):
#         super().__init__(name,age)
#         self.lang=lang

#     def func1(self):
#         super().func1()
#         print("hello Gaurika i am good") 


# p1=Person()
# p1.func1()

# p2=Gaurika("Guarika",34,"Python")
# p2.func1()


# class Book:

#     def __init__(self,name):
#         self.name=name

#     def __len__(self):
#         return len(self.name)
    
#     def __str__(self):
#         return f"My book name is: {b1.name}"

# b1=Book("The Alchemist")

# print(b1)
# print(len(b1))

# print(b1)
# print(dir(Book))

class Vector:
    def __init__(self,xpoint,ypoint):
        self.xpoint=xpoint
        self.ypoint=ypoint

    def showVector(self):
        return f"My vector is: {self.xpoint}i + {self.ypoint}j"
    
    def __add__(self, other):
        self.xpoint=self.xpoint+other.xpoint
        self.ypoint=self.ypoint+other.ypoint
        return Vector(self.xpoint,self.ypoint)
    
v1=Vector(4,7)
v2=Vector(3,6)

print(v1.showVector())
print(v2.showVector())
p3=v1+v2

print(p3.showVector())
