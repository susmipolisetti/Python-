balance = 1000

while True:
    print("\n===== ATM System =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit Successful")
        print("Current Balance:", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful")
            print("Current Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
