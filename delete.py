
import os
# if os.path.exists("day1.py"):
#     print("File exists")
# else:
#     print("Not found")

# folder="D:\Cadd Mentor\Student_Class_Code\Gaurika_Python"
# file="notes.txt"
# full_path = os.path.join(folder, file)
# print(full_path)

# print(os.path.isfile("file.txt")) # True if it is a file
# print(os.path.isdir("foldername")) # True if it is a folder

# print(os.environ)
# print(os.getenv("PATH"))


# a=7
# b=4
# y=9

# b,a,y=a,b,y
# print(a)
# print(b)
# print(y)

# a=9
# b=4

# a=a+b
# b=a-b
# a=a-b

# c=a
# a=b
# b=c

# print(a)
# print(b)

# def evenOdd(num):
#     even=False
#     if(num%2==0):
#         even=True
#     return even

# print(evenOdd(56))

# str1="Shubham"

# print(str1[::-1])
# rev=""
# for i in (str1):
#     rev=i+rev
# for i in range(len(str1)-1,-1,-1):
#     rev=rev+str1[i]

# print(rev)

# list1=[5,2,4,8,4,8,2,8]

# l2=[i for i in list1 if(list1.i)]

# from functools import lru_cache
# import time
# @lru_cache(maxsize=3) # No limit on number of cached calls
# def square(n):
#     time.sleep(2)
#     print(f"Calculating square of {n}")
#     return n * n

# square(2)  # store
# square(3)  # store
# square(4)  # store
# square(5)  # new → 2 wala delete ho jayega
# print(square(2))  # new → 2 wala delete ho jayega

# import re
# text = "My phone number@nuber.com number is 123-456-7890"

# # t1=re.search(r"p..ne",text)
# # t1=re.search(r"\d\d",text)
# t1=re.findall(r'\w+@\w+\.\w+',text)
# # print(t1.group())
# print(t1)

# import asyncio

# str1="Hello Hii kaise ho"

# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 done")
# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 done")

# async def main():
#     await asyncio.gather(task1(), task2())
# asyncio.run(main())

import threading
import time

# shared_string = "Start"

# def modify_string(thread_id):
#     global shared_string
    
#     for i in range(3):
#         # Step 1: Read
#         temp = shared_string
#         print(f"Thread {thread_id} read: {temp}")
        
#         # Artificial delay (race create karne ke liye)
#         time.sleep(0.5)
        
#         # Step 2: Modify
#         temp = temp + f"_{thread_id}"
        
#         # Step 3: Write back
#         shared_string = temp
#         print(f"Thread {thread_id} wrote: {shared_string}")

# # Create multiple threads
# threads = []
# for i in range(3):
#     t = threading.Thread(target=modify_string, args=(i,))
#     threads.append(t)
#     t.start()

# # Wait for all threads
# for t in threads:
#     t.join()

# print("\nFinal String:", shared_string)


# str1="Hello"
# str2="Kumar"
# str3=""

# def update1(strnew1):
#     global str3
#     for item in strnew1:
#         str3+=item
#         time.sleep(1)

# def update2(strnew2):
#     global str3
#     for item in strnew2:
#         str3+=item
#         time.sleep(1)

# t1 = threading.Thread(target=update1, args=(str1,)) 
# t2 = threading.Thread(target=update2, args=(str2,)) 

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(str3)

# from multiprocessing import Pool

# gt=1
# def square(n):
#     global gt
#     print("hello",gt)
#     gt+=1
#     time.sleep(3)
#     return n * n

# if __name__ == "__main__":
#     with Pool(processes=4) as pool:
#         result = pool.map(square, [1, 2, 3, 4,5,6])
#         print(result)   # Output: [1, 4, 9, 16]

# def info(**data):
#     print(data)

# info(name="Neeraj", age=23)

# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def area1(self):
#         return 10 * 5

# r = Rectangle()
# print(r.area())


# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password",
#     database="college"
# )

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM students")

# for row in cursor:
#     print(row)

# conn.close()

# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('./index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     print(username)
#     print(password)

#     if username == "admin" and password == "1234":
#         return "Login Successful "
#     else:
#         return "Invalid Credentials "

# if __name__ == '__main__':
#     app.run(debug=True)