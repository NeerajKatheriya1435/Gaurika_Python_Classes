
# var1=67.56

# print(var1)
# print(type(var1))

# a=47
# b=8
# division=int(a/b)
# print(division)

# a=input("Enter you name: ")
# b=5
# print("My name is:",a)

# a="Abhay"
# b="Kumar"
# print(a+b)

# num1=int(input("Enter number 1: "))
# num2=int(input("Enter number 2: "))

# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1/num2)

# for i in range(5,11,2):
#     print(i)

# for i in range(11,1,-1):
#     print(i)

# import math as m
# a=9.67
# print(math.sqrt(a))
# print(math.ceil(a))

# print(m.sqrt(64))

import turtle

screen=turtle.Screen()
screen.bgcolor("black")

t1=turtle.Turtle()
t1.speed(0)

colors=["blue","red","yellow","white","green"]

for i in range(360):
    t1.pencolor(colors[i%5])
    t1.circle(i*0.5)
    t1.left(10)
turtle.done()