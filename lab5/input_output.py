#1 Basic Input
name = input("Enter your name: ")
print("Hello, ", name)

#2 Type Conversion with Input
age = int(input("Enter your age: "))
print("Next year, you will be ", age + 1)

#3 Multiple Inputs
a, b = input("Enter two numbers separated by space: ").split()
a, b = int(a), int(b)
print("Sum: ", a + b)