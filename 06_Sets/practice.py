# ==========================
# Sets Practice in Python
# ==========================


# Creating Set

numbers = {10,20,30,40}

print(numbers)


# Duplicate Values Removed

data = {1,2,2,3,3,4}

print(data)


# Empty Set

empty_set = set()

print(type(empty_set))


# Adding Element

numbers.add(50)

print(numbers)


# Adding Multiple Elements

numbers.update([60,70,80])

print(numbers)


# Removing Element

numbers.remove(20)

print(numbers)


# Discard Method

numbers.discard(100)

print(numbers)


# Pop Method

values = {1,2,3,4}

values.pop()

print(values)


# Clear Method

temp = {10,20,30}

temp.clear()

print(temp)


# Set Length

skills = {"Python","SQL","Excel"}

print(len(skills))


# Loop Through Set

for skill in skills:
    print(skill)


# Union

set1 = {1,2,3}

set2 = {3,4,5}

print(set1.union(set2))


# Intersection

print(set1.intersection(set2))


# Difference

print(set1.difference(set2))


# Symmetric Difference

print(set1.symmetric_difference(set2))


# Using Operators

print(set1 | set2)

print(set1 & set2)

print(set1 - set2)

print(set1 ^ set2)


# Check Element Exists

if 2 in set1:
    print("Exists")


# Convert List to Set

numbers = [1,2,2,3,4,4]

unique_numbers = set(numbers)

print(unique_numbers)


# Frozen Set

fixed = frozenset([1,2,3])

print(fixed)
