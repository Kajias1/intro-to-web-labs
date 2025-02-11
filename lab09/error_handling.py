# ZeroDivisionError
print(10 / 0)

# ValueError
x = int("abc")

# IndexError
lst = [1, 2, 3]
print(lst[5])

# KeyError
my_dict = {"name": "Alice"}
print(my_dict["age"])

# TypeError
print("2" + 2)

# FileNotFoundError
open("non_existent_file.txt")

# Exception handling using "try" and "except"
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid integer.")

# Catching multiple exceptions
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except (ZeroDivisionError, ValueError):
    print("Error: Invalid operation.")

# Using "else" in exception handling
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Result", result)

# Using "finally"
try:
    file = open("example.txt", "r")
    content =  file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file.")
    file.close()

# Raising exceptinos
def withdraw(amount, balance):
    if (amount > balance):
        raise ValueError("Insufficient balance.")
    return balance - amount

try:
    new_balance = withdraw(200, 100)
except ValueError as e:
    print(f"Error: {e}")

# Raising NotImplementedError
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the `area` method.")

# Custom exceptions
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed"):
        self.message = message
        super().__init__(self.message)

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot compute the square root of a negative number.")
    return number ** 0.5

try:
    result = square_root(-9)
except NegativeNumberError as e:
    print(f"Error {e}")

# Hierarchy of custom exceptions
class ApplicationError(Exception):
    """Base class for all application-related errors."""
    pass

class DatabaseError(ApplicationError):
    """Raised for database-related issues."""
    pass

class ValidationError(ApplicationError):
    """Raised for input validation errors."""
    pass

try:
    raise ValidationError("Invalid input data")
except ValidationError as e:
    print(f"Validation error: {e}")
except ApplicationError as e:
    print(f"Application error: {e}")

