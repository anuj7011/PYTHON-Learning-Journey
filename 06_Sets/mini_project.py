print("===== Student Skills Analyzer =====")


student1 = {
    "Python",
    "SQL",
    "Excel",
    "Power BI"
}


student2 = {
    "Python",
    "SQL",
    "Tableau",
    "Machine Learning"
}


print("\nStudent 1 Skills:")
print(student1)


print("\nStudent 2 Skills:")
print(student2)


print("\nCommon Skills:")
print(student1.intersection(student2))


print("\nAll Skills:")
print(student1.union(student2))


print("\nUnique Skills of Student 1:")
print(student1.difference(student2))


print("\nUnique Skills of Student 2:")
print(student2.difference(student1))
