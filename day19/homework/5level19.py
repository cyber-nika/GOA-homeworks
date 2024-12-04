# Initialize the correct password and incorrect attempt count
correct_password = "Goa best"
incorrect_attempts = 0

# While loop to keep asking for the password until the correct one is entered
while True:
    # Taking input from the user
    password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if password == correct_password:
        print("Password correct! Access granted.")
        break  # Exit the loop when the correct password is entered
    else:
        incorrect_attempts += 1
        print(f"Incorrect password. Attempt {incorrect_attempts}.")

# Print the number of incorrect attempts after the correct password is entered
print(f"You made {incorrect_attempts} incorrect attempts.")
