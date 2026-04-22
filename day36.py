

# class GaurikaError(Exception):
#     pass

# age=int(input("Enter your age: "))

# if(age<0):
#     raise ValueError("Age can not be Negative")
# if(age>150):
#     raise GaurikaError("Age can not be greater than 120")

# if(age>18):
#     print("You can drive the car")
# else:
#     print("You can not drive the car")

# def addTwoNum(num1,num2):
#     # print("hellojiov")
#     pass

# class Dog:
#     def speak(self):
#         print("Bark")
# class Cat(Dog):
#     def speak(self):
#         print("Meow")


# def make_sound(animal):
#     animal.speak()


# d = Dog()
# c = Cat()

# make_sound(d)
# make_sound(c)

# d.speak()
# c.speak()


# class Human:
#     def run(self):
#         print("Hello I am running")
#     def eat(self):
#         print("Hello I am eating")

# class Teacher(Human):
#     def laugh(self):
#         print("Hello I am Laughing")

# h1=Human()
# h1.eat()

# t1=Teacher()
# t1.eat()
# t1.laugh()

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def side(self):
#         pass

#     @abstractmethod
#     def name(self):
#         pass


# class Rectangle(Shape):
#     def area(self):
#         return 10 * 5
    
#     def side(self):
#         return 56
        
#     def name(self):
#         return 78
    
# r = Rectangle()
# print(r.area())

# nums = [1, 2, 3]
# it = iter(nums)

# print(next(it)) # 1
# print(next(it)) # 2
# print(next(it)) # 3

# l1=[i for i in range(12) if i%2==0]
# print(l1)

# s = {x*x for x in range(5)}
# print(s)

# d = {x: x*x for x in range(5)}
# print(d)
import numpy
a1=numpy.array([4,6,7,])

print(a1)