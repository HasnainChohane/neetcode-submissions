#class with functions 
class Person:
    def __init__ (self  , name ,age):
        self.name = name
        self.age = age
name = input("Enter your Name : ")
age = input("Enter your age : ")
p1 = Person(name,age)
print(p1.name)
print(p1.age)