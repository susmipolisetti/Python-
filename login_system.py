username = "admin"
password = "1234"

user = input("Enter Username: ")
pwd = input("Enter Password: ")

if user == username and pwd == password:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")
