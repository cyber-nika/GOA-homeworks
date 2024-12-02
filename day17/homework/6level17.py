# Define the correct username and password
correct_username = "user123"
correct_password = "mypassword123"

# Prompt the user for username and password, and keep asking until both are correct
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful. Access granted!")
        break  # Exit the loop if both username and password are correct
    else:
        print("Incorrect username or password. Please try again.")