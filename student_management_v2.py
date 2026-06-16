
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
File: student_management_v2.py
