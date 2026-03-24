class Mother:
    def details(self):
        print("Hello I am Mother")

class Father:
    def details(self):
        print("Hello I am Father")

class Son(Mother,Father):
    def speak(self):
        print("Hello i am son")

# s1=Son()

# s1.details()
print(Son.__mro__)