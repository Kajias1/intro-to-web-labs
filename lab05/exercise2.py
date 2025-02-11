name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Your name is saved as - ", name, ", and your age as - ", age)

a, b, c = input("Enter three numbers separated by space: ").split()
a, b, c = int(a), int(b), int(c)
print("Sum: ", a + b + c)
print("Average: ", (a + b + c) / 3)
print("Product: ", a * b * c)