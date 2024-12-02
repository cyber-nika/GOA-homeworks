# Prompt the user for a number
num = int(input("Enter a number to calculate its factorial: "))

# Initialize variables
factorial = 1
count = 1

# Ensure that the number is a non-negative integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Use while loop to calculate factorial
    while count <= num:
        factorial *= count
        count += 1
    
    # Print the result
    print(f"The factorial of {num} is {factorial}.")
