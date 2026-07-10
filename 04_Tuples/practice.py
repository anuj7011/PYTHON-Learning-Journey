# ==========================
# Tuples Practice in Python
# ==========================


# Creating Tuple

numbers = (10,20,30,40)

print(numbers)


# Tuple with different data types

data = ("Anuj",20,5.8,True)

print(data)


# Empty Tuple

empty_tuple = ()

print(empty_tuple)


# Single Element Tuple

single = (10,)

print(single)


# Accessing Elements

names = ("Anuj","Ravi","Aman")

print(names[0])
print(names[-1])


# Tuple Length

print(len(names))


# Tuple Slicing

values = (1,2,3,4,5)

print(values[1:4])
print(values[::-1])


# Tuple Concatenation

tuple1 = (1,2,3)
tuple2 = (4,5,6)

print(tuple1 + tuple2)


# Tuple Repetition

print((1,2)*3)


# Count Method

numbers = (1,2,2,3,2,4)

print(numbers.count(2))


# Index Method

cities = ("Delhi","Mumbai","Pune")

print(cities.index("Mumbai"))


# Tuple Packing

student = "Anuj",20,"Python"

print(student)


# Tuple Unpacking

name,age,course = student

print(name)
print(age)
print(course)


# Nested Tuple

employee = (
    (101,"Anuj"),
    (102,"Ravi")
)

print(employee[0][1])


# Loop Through Tuple

languages = ("Python","SQL","Excel")

for lang in languages:
    print(lang)


# Convert Tuple to List

my_tuple = (1,2,3)

my_list = list(my_tuple)

print(my_list)


# Convert List to Tuple

list1 = [10,20,30]

tuple1 = tuple(list1)

print(tuple1)
