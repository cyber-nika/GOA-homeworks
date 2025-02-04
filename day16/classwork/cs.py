# Get input from the user and convert it to an integer
num = int(input("Enter a number: "))

# Initialize sum variable
total = 0

# Loop through the range and sum up the numbers
for i in range(num + 1):
    total += i

# Print the total sum
print("The sum of numbers from 0 to", num, "is:", total)
