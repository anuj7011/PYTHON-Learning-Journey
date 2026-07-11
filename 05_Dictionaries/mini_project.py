print("===== Student Information System =====")


student = {}


student["name"] = input("Enter Student Name: ")
student["age"] = int(input("Enter Age: "))
student["course"] = input("Enter Course: ")
student["marks"] = int(input("Enter Marks: "))


print("\nStudent Details")

for key,value in student.items():
    print(key,":",value)


# Update Marks

new_marks = int(input("\nEnter Updated Marks: "))

student.update({
    "marks":new_marks
})


print("\nUpdated Details")

print(student)
