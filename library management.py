books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nBooks List:")
            for book in books:
                print(book)

    elif choice == "3":
        book = input("Enter book name to search: ")

        if book in books:
            print("Book found!")
        else:
            print("Book not found.")

    elif choice == "4":
        book = input("Enter book name to remove: ")

        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
