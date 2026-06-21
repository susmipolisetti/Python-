tasks = []

while True:
    print("\n===== To-Do List =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for task in tasks:
            print(task)

    elif choice == "3":
        task = input("Enter task to remove: ")

        if task in tasks:
            tasks.remove(task)
            print("Task Removed")
        else:
            print("Task Not Found")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
