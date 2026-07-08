# ==========================
# Strings Practice in Python
# ==========================


# Creating Strings

name = "Anuj"
city = 'Delhi'

print(name)
print(city)


# String Length

message = "Python Learning"

print(len(message))


# String Indexing

text = "Python"

print(text[0])
print(text[1])
print(text[-1])


# String Slicing

word = "Programming"

print(word[0:6])
print(word[:5])
print(word[3:])
print(word[::-1])


# String Concatenation

first_name = "Anuj"
last_name = "Chauhan"

full_name = first_name + " " + last_name

print(full_name)


# String Repetition

print("Python " * 3)


# Upper and Lower

language = "python"

print(language.upper())
print(language.lower())


# Title Method

sentence = "python programming"

print(sentence.title())


# Strip

data = "   Python   "

print(data.strip())


# Replace

text = "I love Java"

print(text.replace("Java","Python"))


# Find

course = "Data Analytics"

print(course.find("Analytics"))


# Count

word = "banana"

print(word.count("a"))


# Startswith

name = "Python"

print(name.startswith("Py"))


# Endswith

file = "python.py"

print(file.endswith(".py"))


# Split

skills = "Python,SQL,Excel"

print(skills.split(","))


# Join

items = ["Python","SQL","Power BI"]

print("-".join(items))


# Escape Character

print("Hello\nPython")

print("Hello\tPython")


# f-string

name = "Anuj"
age = 20

print(f"My name is {name} and my age is {age}")


# Input String

user_name = input("Enter your name: ")

print("Welcome", user_name)
