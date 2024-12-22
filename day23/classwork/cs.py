# List with 10 elements
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# User input
user_input = int(input("Please enter a number: "))

# If the number is greater than or equal to 0 and less than the length of the list
if 0 <= user_input < len(my_list):
    print(f"The element at index {user_input} is: {my_list[user_input]}")

# If the number is greater than or equal to -1 and less than or equal to the negative length of the list
elif len(my_list) * -1 <= user_input <= -1:
    print(f"The element at index {user_input} is: {my_list[user_input]}")
else:
    print("The entered number is out of the allowed range.")


