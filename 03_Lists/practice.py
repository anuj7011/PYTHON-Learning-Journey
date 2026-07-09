# ==========================
# Lists Practice in Python
# ==========================


# Creating Lists

numbers = [10,20,30,40]

names = ["Anuj","Ravi","Aman"]

mixed = ["Python",100,5.5,True]


print(numbers)
print(names)
print(mixed)


# Accessing Elements

print(numbers[0])
print(numbers[-1])


# List Length

print(len(numbers))


# Slicing

marks = [50,60,70,80,90]

print(marks[1:4])
print(marks[:3])
print(marks[::-1])


# Updating List

marks[0] = 100

print(marks)


# Append

numbers.append(50)

print(numbers)


# Insert

numbers.insert(1,15)

print(numbers)


# Extend

numbers.extend([60,70])

print(numbers)


# Remove

numbers.remove(20)

print(numbers)


# Pop

numbers.pop()

print(numbers)


# Delete

del numbers[0]

print(numbers)


# Clear

temp = [1,2,3]

temp.clear()

print(temp)


# Index

students = ["Rahul","Anuj","Aman"]

print(students.index("Anuj"))


# Count

data = [1,2,2,3,2,4]

print(data.count(2))


# Sort

values = [5,2,8,1]

values.sort()

print(values)


# Reverse

values.reverse()

print(values)


# Copy

list1 = [10,20,30]

list2 = list1.copy()

print(list2)


# Loop Through List

for item in students:
    print(item)


# Nested List

student = [
    ["Anuj",20],
    ["Rahul",21]
]

print(student[0][0])
