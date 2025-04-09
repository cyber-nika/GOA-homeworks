try:
    user_input = input("Enter a number: ")
    number = float(user_input)  # using float to accept decimals too
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: That's not a valid number!")