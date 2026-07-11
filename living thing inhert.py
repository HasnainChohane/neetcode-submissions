class LivingThing:
    def breathe(self):
        print("Breathing...")

class Animal(LivingThing):
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Creating an object
my_dog = Dog()
my_dog.breathe()
my_dog.eat()
my_dog.bark()
