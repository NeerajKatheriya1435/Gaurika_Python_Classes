
# age=34

# if(age>18):
#     print("You are eligible for vote")
#     if(age==45):
#         print("You are in special age")
#     else:
#         print("You are not good")
# else:
#     print("You are not elible")

# marks=95

# if(marks>90):
#     print("Excellent")
# elif(marks>75):
#     print("Grade A")
# elif(marks>60):
#     print("Grade B")
# elif(marks>35):
#     print("Grade C")
# else:
#     print("Fail")

# Task1
# age=45

# if(age>18 and age<80):
#     print("You can drive the car")
# else:
#     print("You can not drive the car")


# Match Case Statements

# opt=47

# match(opt):
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Thursday")
#     case _:
#         print("Please input value between 1 to 4")

# num1=int(input("Enter the number 1: "))
# num2=int(input("Enter the number 1: "))
# opt=input("Please choose a input +,-,*,/: ")

# match(opt):
#     case "+":
#         print(num1+num2)
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Thursday")
#     case _:
#         print("Please input value between 1 to 4")

# opt=int(input("Enter number1: "))
# match(opt):
#     case 1|6|9|8:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Thursday")
#     case _:
#         print("Please input value between 1 to 4")

# opt=int(input("Enter number1: "))
# match(opt):
#     case 1|6|9|8:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Thursday")
#     case _ if(opt==45):
#         print("My value is 45")
#     case _ :
#         print("Final Default case")

# number = 45
# match number:
#     case _ if number % 2 == 0:
#         print("Even number")
#     case _:
#         print("Odd number")