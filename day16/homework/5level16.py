# Define the correct username and password
correct_username = "user123"
correct_password = "secure123"

# Initialize variables to store the user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Keep asking until both username and password are correct
while username != correct_username or password != correct_password:
    print("Incorrect username or password. Try again.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

# Once both username and password are correct
print("Login successful! Access granted.")
