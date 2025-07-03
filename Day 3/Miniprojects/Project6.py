# 🔥 6. Login Authentication System
correct_username = "admin"
correct_password = "1234"

username = input("Username: ")
password = input("Password: ")

if username is correct_username and password is correct_password:
    print("Login Successful")
else:
    print("Login Failed")