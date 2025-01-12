my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# მომხმარებლის მიერ შეყვანილი რიცხვები
num1 = int(input("Enter the first number (index): "))
num2 = int(input("Enter the second number (index): "))

if num1 > num2:
    print(my_list[num1:num2])
elif num2 > num1:
    print(my_list[num2:num1])
else:
    print([])
