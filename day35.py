# from multiprocessing import Process
# import time

# def calculate_square(numbers):
#     print("Squares:")
#     for n in numbers:
#         time.sleep(2)
#         print(f"{n}^2 = {n*n}")

# def calculate_cube(numbers):
#     print("Cubes:")
#     for n in numbers:
#         time.sleep(2)
#         print(f"{n}^3 = {n*n*n}")

# def calculate_cube(numbers):
    
#     print("Cubes:")
#     for n in numbers:
#         time.sleep(2)
#         print(f"{n}^3 = {n*n*n}")

# if __name__ == "__main__":
#     nums = [2, 3, 4, 5]
#     # Create processes
#     p1 = Process(target=calculate_square, args=(nums,))
#     p2 = Process(target=calculate_cube, args=(nums,))
#     # Start processes
#     p1.start()
#     p2.start()
#     # Wait for processes to finish
#     p1.join()
#     p2.join()
#     print("Done with multiprocessing!")

# import re
# text="My name is neeraj and abhay is good hari@gmail.com"
# # pattern=re.compile(r'\w+@+\w+.+\w+')
# pattern=re.compile(r'[adn]')
# data=pattern.findall(text)
# print(data)

# def sum(num):
#     s=0
#     for i in range(1,num+1):
#         s+=i
#         print()
#     return s

# print(sum(6))

# def add(a, b=80):
    # print(a)
    # print(b)
    # print(a + b)

# add(5, 3)
# add(b=3,a=5)
# add(4,9)
# add(4)

def sum1(*num):
    print(num)
    # print(sum(num))

# def sum1(**num):
#     print(num)
    # print(sum(num))
    # return s

# t1=(4,7,3,8,3)
# l1=[6,4,5,7,4]
# sum1(l1)

# sum1(name="Rohan",age=78)

# def func()
#     print("Hello")

try:
    # a = 10
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    print(a / b)
# except Exception as e:
#     print(e)
except ZeroDivisionError:
    print("Zero Divisble not poss")

except ValueError:
    print("Value erro program")

finally:
    print("Last line")

print("Important line")



# func()