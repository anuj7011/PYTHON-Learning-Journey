# ==============================
# Dictionaries Practice in Python
# ==============================


# Creating Dictionary

student = {
    "name": "Anuj",
    "age": 20,
    "course": "Python"
}

print(student)


# Accessing Values

print(student["name"])
print(student["age"])


# Using get()

print(student.get("course"))


# Adding New Key

student["city"] = "Delhi"

print(student)


# Updating Value

student["age"] = 21

print(student)


# Removing Value using pop()

student.pop("city")

print(student)


# popitem()

student.popitem()

print(student)


# Dictionary Length

data = {
    "a":1,
    "b":2,
    "c":3
}

print(len(data))


# Keys Method

employee = {
    "id":101,
    "name":"Anuj",
    "salary":45000
}

print(employee.keys())


# Values Method

print(employee.values())


# Items Method

print(employee.items())


# Checking Key Exists

if "name" in employee:
    print("Key Exists")


# Update Method

employee.update({
    "department":"IT"
})

print(employee)


# Copy Dictionary

copy_data = employee.copy()

print(copy_data)


# Clear Dictionary

temp = {
    "x":10,
    "y":20
}

temp.clear()

print(temp)


# Loop Through Dictionary

for key in employee:
    print(key)


for value in employee.values():
    print(value)


for key,value in employee.items():
    print(key,value)


# Nested Dictionary

students = {

    "student1":{
        "name":"Anuj",
        "marks":90
    },

    "student2":{
        "name":"Ravi",
        "marks":85
    }
}


print(students["student1"]["name"])


# Dictionary Comprehension

square = {
    x:x*x for x in range(1,6)
}

print(square)
