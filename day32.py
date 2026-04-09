# num=5
# for i in range(num):
#     value=1
#     for k in range(num-i-1,-1,-1):
#          print(" ",end="")
#     for j in range(i+1):
#          print(value,end=" ")
#          value=value*(i-j)//(j+1)
#     print()

"""
i   j   value   calculation
0   0   1       0
1   0   1       1
1   1   1       0
"""


#      1
#     1 1
#    1 2 1

# num=

# 1
# 11
# 121
# 1331

#     1
#    2 2
#   3 3 3

# num=5
# for i in range(num):
#     for j in range(num-i-1,-1,-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")
#     print()

# num=8
# for i in range(num,-1,-1):
#     for k in range(num-i):
#         print(" ",end="")
#     for j in range(2*i+1,0,-1):
#         print("*",end="")
#     print()

# for i in range(2):
#     print("*")

#   *
#  ***

# *******
#  *****
# num=5

# for i in range(num):
#     print(" "*(num-i-1)+"*"*(2*i+1))
# for k in range(num):
#     print(" "*(k+1)+"*"*(2*(num-k-1)-1))

num=5
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range((2*i)-1):
        if(i==1 or i==num or k==0 or k==(2*i)-2):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# Count frequency of each character.

str1="Hellolllhhh"

# freq={}

# for i in str1:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1

# print(freq)

# a=8
# b=7
# b,a=a,b
# print(a,b)

# a=a+b # a=15
# b=a-b # 15-7=8
# a=a-b
# print(a,b)

