# Define the correct password
correct_password = "mypassword123"

# Prompt the user to enter a password and keep asking until it's correct
user_password = input("Enter the password: ")

while user_password != correct_password:
    print("Incorrect password. Please try again.")
    user_password = input("Enter the password: ")

# When the correct password is entered
print("Password accepted. Access granted!")