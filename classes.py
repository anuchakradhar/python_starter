# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#create class
class Person:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def greeting(self):
        print(f'My name is {self.name} and I am {self.age} years old')
    
    def has_birthday(self):
        self.age += 1

class Customer(Person):
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        print(f'My name is {self.name} and I am {self.age} years old and my balance is {self.balance}')

#init person
p1 = Person('Anu', 24)
p1.has_birthday()
p1.greeting()

#init customer
c1 = Customer('Sanu', 25)
c1.set_balance(2500)
c1.greeting()