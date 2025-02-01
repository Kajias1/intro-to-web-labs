# Defining a simple class and creating an object

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.brand} {self.model} ({self.year})"

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)

print(car1.display_info())
print(car2.display_info())

# Adding methods to a class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())

# Changing object attributes

class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
phone1 = Phone("Samsung", 500)
print(phone1.price)

phone1.price = 450
print(phone1.price)

# Class vs Instance variables

class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

print(e1.company)
print(e2.company)

Employee.company = "NewTechCorp"

print(e1.company)
print(e2.company)

# The role of "self" keyword

class Calculator:
    def __init__(self, value):
        self.value = value
    
    def add(self, num):
        self.value += num
    
    def get_value(self):
        return self.value

calc = Calculator(10)
calc.add(5)
print(calc.get_value())

# Deleting attributes and objects

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
user1 = User("john_doe", "john@example.com")
print(user1.email)

del user1.email
# print(user1.email) -> AttributeError

del user1
# print(user1.username) -> NameError
