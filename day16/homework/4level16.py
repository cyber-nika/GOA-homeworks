# Define the correct password
correct_password = "secure123"

# Ask the user to enter the password
user_input = input("Enter your password: ")

# Keep asking until the user enters the correct password
while user_input != correct_password:
    print("Incorrect password. Try again.")
    user_input = input("Enter your password: ")

# Once the correct password is entered
print("Password accepted. Access granted.")
