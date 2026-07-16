print("===== Student Grade Calculator =====")

def calculate_total(marks):
    return sum(marks)

def calculate_average(total, count):
    return total / count

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    return "Fail"

marks = []

for i in range(5):
    mark = int(input(f"Enter Marks {i+1}: "))
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(total, len(marks))
grade = calculate_grade(average)

print("\n===== Result =====")
print("Total   :", total)
print("Average :", average)
print("Grade   :", grade)
