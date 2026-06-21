expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)

    elif choice == "2":
        print(expenses)

    elif choice == "3":
        print("Total Expense:", sum(expenses))

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
