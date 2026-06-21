employees = {}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        employees[emp_id] = name
        print("Employee Added Successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No Employees Found.")
        else:
            for emp_id, name in employees.items():
                print(emp_id, "-", name)

    elif choice == "3":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            print("Employee Name:", employees[emp_id])
        else:
            print("Employee Not Found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID: ")

        if emp_id in employees:
            del employees[emp_id]
            print("Employee Deleted Successfully!")
        else:
            print("Employee Not Found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
