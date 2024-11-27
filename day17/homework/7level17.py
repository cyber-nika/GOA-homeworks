# Prompt the user for a number
num = int(input("Enter a number to calculate its factorial: "))

# Initialize the factorial result and counter
factorial = 1
counter = 1

# Use a while loop to calculate the factorial
while counter <= num:
    factorial *= counter  # Multiply the current factorial by the counter
    counter += 1  # Increment the counter

# Print the result
print(f"The factorial of {num} is {factorial}")