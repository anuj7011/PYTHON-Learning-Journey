print("===== Student Result System =====")


name = input("Enter Student Name: ")

marks = int(input("Enter Marks: "))


if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 50:
    grade = "C"

else:
    grade = "Fail"


status = "Pass" if marks >=40 else "Fail"


print("\nStudent Result")

print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Status:", status)
