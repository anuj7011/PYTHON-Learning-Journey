# ==========================
# Loops Practice in Python
# ==========================


# For Loop

for i in range(5):
    print(i)


# Range with Start and End

for i in range(1,6):
    print(i)


# Range with Step

for i in range(0,10,2):
    print(i)


# Loop Through String

name = "Python"

for char in name:
    print(char)


# Loop Through List

skills = ["Python","SQL","Excel"]

for skill in skills:
    print(skill)


# Loop Through Tuple

numbers = (10,20,30)

for num in numbers:
    print(num)


# Loop Through Dictionary

student = {
    "name":"Anuj",
    "age":20,
    "course":"Python"
}


for key,value in student.items():
    print(key,value)


# While Loop

count = 1

while count <=5:
    print(count)
    count +=1


# Break Statement

for i in range(1,10):

    if i == 5:
        break

    print(i)


# Continue Statement

for i in range(1,6):

    if i == 3:
        continue

    print(i)


# Pass Statement

for i in range(5):
    pass


# Nested Loop

for i in range(1,4):

    for j in range(1,4):

        print(i,j)


# Multiplication Table

num = 5

for i in range(1,11):
    print(num*i)


# Sum of Numbers

total = 0

for i in range(1,11):
    total += i

print(total)


# Factorial

number = 5
fact = 1

for i in range(1,number+1):
    fact *= i

print(fact)
