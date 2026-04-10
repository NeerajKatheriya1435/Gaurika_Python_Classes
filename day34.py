# import time

# def task1():
#     time.sleep(2)
#     print("Task 1 done")
# def task2():
#     time.sleep(2)
#     print("Task 2 done")

# task1()
# task2()

# import asyncio

# async def task1():
#     await asyncio.sleep(2)
#     print("Task 1 done")
# async def task2():
#     await asyncio.sleep(2)
#     print("Task 2 done")
# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())

# import threading
# import time

# def display():
#     for i in range(10):
#         print(f"Thread running: {i}")
#         time.sleep(1)

# t1 = threading.Thread(target=display)

# t1.start()

# for i in range(5):
#     print(f"Main thread: {i}")
#     time.sleep(1)

# t1.join()

# print("Program finished")


from multiprocessing import Process

def calculate_square(numbers):
    print("Squares:")
    for n in numbers:
        print(f"{n}^2 = {n*n}")

def calculate_cube(numbers):
    print("Cubes:")
    for n in numbers:
        print(f"{n}^3 = {n*n*n}")

if __name__ == "__main__":
    nums = [2, 3, 4, 5]

    # Create processes
    p1 = Process(target=calculate_square, args=(nums,))
    p2 = Process(target=calculate_cube, args=(nums,))

    # Start processes
    p2.start()
    p1.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print("Done with multiprocessing!")
