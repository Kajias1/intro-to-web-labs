# Lists

fruits = ["apple", "banana", "cherry"]

print(fruits[0])

fruits.append("orange")

fruits.remove("banana")

for fruit in fruits:
    print(fruit)

# Dictionaries

student = {"name": "John", "age": 22, "grade": "A"}

print(student["name"])

student["age"] = 23

for key, value in student.items():
    print(f"{key}: {value}")

# Sets

numbers = {1, 2, 3, 4, 5}

numbers.add(6)

numbers.remove(3)

evens = {2, 4, 6, 8}
print(numbers.intersection(evens))

# Tuples

point = (10, 20)

print(point[0])

for coord in point:
    print(coord)

# Tracking Inventory

inventory = {"apples": 50, "oranges": 30, "bananas": 20}

inventory["apples"] += 10

if inventory["oranges"] < 10:
    print("Restock oranges!")

# Removing duplicates

emails = ["user1@example.com", "user2@example.com", "user1@example.com"]
unique_emails = set(emails)
print(unique_emails)

# Immutable Data

location = (37.7749, -122.4194)
print(f"Latitude: {location[0]}, Longitude: {location[1]}")

