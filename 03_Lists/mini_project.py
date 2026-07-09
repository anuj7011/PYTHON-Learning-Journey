print("===== Student Marks Management System =====")


marks = []


while True:

    print("\n1. Add Marks")
    print("2. Remove Marks")
    print("3. Display Marks")
    print("4. Calculate Total")
    print("5. Exit")


    choice = int(input("Enter choice: "))


    if choice == 1:

        mark = int(input("Enter marks: "))
        marks.append(mark)

        print("Marks Added")


    elif choice == 2:

        mark = int(input("Enter marks to remove: "))
        marks.remove(mark)

        print("Marks Removed")


    elif choice == 3:

        print("Marks:", marks)


    elif choice == 4:

        print("Total Marks:", sum(marks))


    elif choice == 5:

        break


    else:

        print("Invalid Choice")
