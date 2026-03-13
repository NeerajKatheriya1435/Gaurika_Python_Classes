class Animal:
    def __init__(self,name,age,rollNum):
        self._public_age=age
        self._protected_rollNum=rollNum
        self.__private_name=name
    def run(self):
        print("Animal is Running....")

a1=Animal("Rohan",45,101)


print(a1._public_age)
print(a1._protected_rollNum)
print(a1._Animal__private_name)
