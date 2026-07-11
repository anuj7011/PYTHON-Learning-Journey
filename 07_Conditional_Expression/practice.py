# =================================
# Conditional Expression Practice
# =================================


# Simple if statement

age = 20

if age >= 18:
    print("Eligible for voting")


# if-else statement

number = 10

if number > 0:
    print("Positive Number")
else:
    print("Negative Number")


# if-elif-else

marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")


# Even Odd Checking

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Multiple Conditions

age = 22
has_license = True

if age >=18 and has_license:
    print("Can Drive")
else:
    print("Cannot Drive")


# OR Operator

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# NOT Operator

is_logged_in = False

if not is_logged_in:
    print("Please Login")


# Nested if

username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("Invalid User")


# Ternary Operator

age = 20

result = "Adult" if age >=18 else "Minor"

print(result)


# Largest Number

a = 10
b = 20

largest = a if a>b else b

print(largest)


# User Input Condition

marks = int(input("Enter Marks: "))

if marks >=40:
    print("Pass")
else:
    print("Fail")
