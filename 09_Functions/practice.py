# ==========================
# Functions Practice in Python
# ==========================

# Simple Function

def welcome():
    print("Welcome to Python!")

welcome()

# Function with Parameter

def greet(name):
    print(f"Hello, {name}")

greet("Anuj")

# Function with Multiple Parameters

def add(a, b):
    print("Sum:", a + b)

add(10, 20)

# Function Returning Value

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)

# Default Parameter

def country(name, place="India"):
    print(name, place)

country("Anuj")
country("John", "USA")

# Keyword Arguments

def student(name, age):
    print(name, age)

student(age=20, name="Anuj")

# Variable-Length Arguments (*args)

def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)

# Keyword Variable-Length Arguments (**kwargs)

def profile(**info):
    for key, value in info.items():
        print(key, value)

profile(name="Anuj", course="Python", city="Delhi")

# Lambda Function

square = lambda x: x * x
print(square(5))

# Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Local Variable

def demo():
    x = 10
    print(x)

demo()

# Global Variable

x = 100

def show():
    print(x)

show()
