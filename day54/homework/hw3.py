# 4. Convert String to Integer
def convert_string_to_int():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print(f"Converted number is: {number}")
    except ValueError:
        print("Error: The input is not a valid number.")