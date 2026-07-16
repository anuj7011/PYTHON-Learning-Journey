# ==========================
# Recursion Practice in Python
# ==========================

# 1. Simple Recursion

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)


# 2. Factorial

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# 3. Sum of Natural Numbers

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print(sum_numbers(10))


# 4. Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")


print()


# 5. Power Function

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 5))


# 6. Reverse String

def reverse(text):
    if len(text) == 0:
        return ""
    return reverse(text[1:]) + text[0]

print(reverse("Python"))


# 7. Find Maximum in List

def maximum(data):
    if len(data) == 1:
        return data[0]
    return max(data[0], maximum(data[1:]))

print(maximum([5, 9, 2, 15, 8]))
