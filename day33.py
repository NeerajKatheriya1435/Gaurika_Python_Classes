
# str1="my name is neeraj number is: 123-456-7890 how are you"

# import re

# text = "My phone gaurika@gmail.com number is 123 and number 346567 and 457"
# pickedValue=re.search(r'\d{3}-\d{3}-\d{4}',text)
# print(pickedValue)

# print(pickedValue.group())
# matches=re.findall(r'\d{3}',text)
# updated=re.sub(r'\w+@\w+\.\w+',"rohan@gmail.com",text)
# print(updated)

# pattern = re.compile(r'\d+')
# print(pattern.findall("I have 2 apples and 10 bananas"))

import time
import asyncio

# async def task1():
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("Hello")

# async def task2():
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("Nice")

# task1()
# task2()

# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())

# import asyncio

# async def fetch_data(site):
#     print(f"Fetching from {site}")
#     await asyncio.sleep(2) # simulate network delay
#     print(f"Done fetching {site}")

# async def main():
#     sites = ['Google', 'YouTube', 'Facebook']
#     tasks = [fetch_data(site) for site in sites]
#     await asyncio.gather(*tasks)

# asyncio.run(main())

# l1=[i for i in range(5)]
# print(l1)
