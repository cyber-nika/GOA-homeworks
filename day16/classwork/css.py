# Set the correct password
correct_password = "mypassword"

# Initialize counter
attempts = 0

while True:
    # Get input from the user
    user_password = input("Enter the password: ")
    attempts += 1

    # Check if the password is correct
    if user_password == correct_password:
        print("Access granted!")
        print("Attempts:", attempts)
        break
    else:
        print("Wrong password, try again.")
