print("===== Recursive Calculator =====")


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


print("1. Factorial")
print("2. Power")
print("3. Sum of Natural Numbers")

choice = int(input("Enter Choice: "))

if choice == 1:
    n = int(input("Enter Number: "))
    print("Factorial:", factorial(n))

elif choice == 2:
    base = int(input("Enter Base: "))
    exponent = int(input("Enter Exponent: "))
    print("Answer:", power(base, exponent))

elif choice == 3:
    n = int(input("Enter Number: "))
    print("Sum:", sum_numbers(n))

else:
    print("Invalid Choice")
