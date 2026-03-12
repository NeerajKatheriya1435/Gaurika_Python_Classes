class Animal:
    def run(self):
        print("Animal is Running....")
    def eat(self):
        print("Animal is Eating....")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Lion(Animal):
    def roar(self):
        print("Lion is Roaring")

a1=Animal()
a1.run()


b1=Dog()
b1.bark()
b1.run()

l1=Lion()
l1.run()
l1.eat()
l1.roar()