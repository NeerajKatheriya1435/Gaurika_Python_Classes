import argparse

# "Sumit-56-20000"

# name="Sumit"
# age=56
# salary=2000
 
parser=argparse.ArgumentParser(description="Simple Calc")
parser.add_argument("num1",type=float)
parser.add_argument("num2",type=float)
parser.add_argument("--operation", "-o", choices=["add", "sub"])

# parser.parse_args("operation",)

args=parser.parse_args()

if args.operation == "add":
    result = args.num1 + args.num2
else:
    result = args.num1 - args.num2
print("Result:", result)

