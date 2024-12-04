for i in range(0, 21, 2):
    print(i)

for i in range(1, 21, 2):
    print(i)

for i in range(10, 31):
    print(f"{i} - {'even' if i % 2 == 0 else 'odd'}")

   # Get two numbers num1 and num2 from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# A variable to store the sum of all the printed numbers
sum_of_numbers = 0

# If the first number is greater than the second, we create a range from num2 to num1 (even numbers only)
if num1 > num2:
    for i in range(num2, num1 + 1):  # Creates the range num2 - num1
        if i % 2 == 0:  # if the number is even
            print(f"{i} - even")  # orint
            sum_of_numbers += i  # Add the number to the total

# If the second number is greater than the first, we create a range from num1 to num2 (odd numbers only)
else:
    for i in range(num1, num2 + 1):  # Creates the range num1 - num2
        if i % 2 != 0:  # if number is odd
            print(f"{i} - odd")  # print
            sum_of_numbers += i  # Add the number to the total

# Final print the sum of all printed numbers
print(f"ჯამი: {sum_of_numbers}")

