# Calculating a square of a number

def square(num):
    return num ** 2

print(square(4))

# Returning a sum of a list of numbers

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4]))

# Recursive Fibonacci sequence function

def next_fibonacci(n):
    if n <= 1:
        return n
    return next_fibonacci(n - 1) + next_fibonacci(n - 2)

print(next_fibonacci(6))

# Function to determine prime numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))