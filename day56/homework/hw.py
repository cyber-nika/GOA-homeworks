# 2) Print your name
print("John Doe")

# 3) Print a favorite quote
print('"The only way to do great work is to love what you do." - Steve Jobs')

# 4) Print multiple lines
print("Roses are red\nViolets are blue\nPython is fun\n")

# 5) Print a simple math result
print("2 + 3 =", 2 + 3)

# 6) Print a shape with symbols
print("*\n**\n***")

# 7) Convert string to integer
num_str = "42"
num_int = int(num_str)
print("Converted:", num_int)

# 8) Add two floats
a = 3.5
b = 2.5
print("Sum of floats:", a + b)

# 9) Concatenate two strings
greeting = "Hello"
name = "World"
print(greeting + " " + name)

# 10) Print data types
x = 5
y = "text"
z = 3.14
print(type(x), type(y), type(z))

# 11) User input and type conversion
age = int(input("Enter your age: "))
print("Next year, you’ll be", age + 1)

# 12) Ask for your name
name = input("What's your name? ")
print("Hello,", name + "!")

# 13) Ask for age and calculate next year’s age
age = int(input("How old are you? "))
print("Next year you'll be", age + 1)

# 14) Simple calculator: addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is", num1 + num2)

# 15) Favorite color
color = input("What's your favorite color? ")
print("Your favorite color is", color + "!")

# 16) Check if the user is tall enough
height = int(input("Enter your height in cm: "))
if height > 150:
    print("You're tall enough!")
else:
    print("You might need to grow a bit more!")

# 17) Print numbers from 1 to 5 using for loop
for i in range(1, 6):
    print(i)

# 18) Print each letter of a string
word = "Python"
for letter in word:
    print(letter)

# 19) Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print("Sum from 1 to 10 is", total)

# 20) Multiplication table for 2
for i in range(1, 6):
    print(f"2 x {i} = {2 * i}")

# 21) Even numbers from 2 to 20
for i in range(2, 21, 2):
    print(i)

# 22) While loop from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 23) Sum of numbers 1 to 5 using while loop
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum from 1 to 5 is", total)

# 24) Countdown from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 25) Print odd numbers between 1 and 10
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

# 26) Ask for user input until they enter "exit"
while True:
    user_input = input("Type something (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    print("You typed:", user_input)

# 27) Print all elements of a list
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)

# 28) Length of a list
print("Length of list:", len(items))

# 29) Access a specific element from the list
numbers = [10, 20, 30, 40]
print("Second element:", numbers[1])

# 30) Add an element to the list
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Updated list:", fruits)

# 31) Remove an element from the list
fruits.remove("banana")
print("After removal:", fruits)

# 32) List of squares (1 to 5)
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

# 33) List of even numbers (2 to 10)
evens = [x for x in range(2, 11) if x % 2 == 0]
print("Even numbers:", evens)

# 34) Filter odd numbers from a list
nums = [1, 2, 3, 4, 5]
odds = [x for x in nums if x % 2 != 0]
print("Odd numbers:", odds)

# 35) Convert strings to uppercase
words = ["hello", "world"]
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)

# 36) Square only even numbers
nums = [1, 2, 3, 4, 5]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print("Squared evens:", even_squares)

# 37) Greet a user with a function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# 38) Add two numbers using a function
def add(a, b):
    return a + b

print("Sum is", add(5, 3))

# 39) Check if a number is even or odd
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print("4 is", check_even_odd(4))

# 40) Area of rectangle
def area(length, width):
    return length * width

print("Area:", area(5, 3))

# 41) Reverse a string
def reverse_string(s):
    return s[::-1]

print("Reversed:", reverse_string("Python"))

# 42) Create and print a tuple
my_tuple = (42, "hello", 3.14)
print("Tuple:", my_tuple)

# 43) Access an element in a tuple
print("Second item:", my_tuple[1])

# 44) Length of a tuple
print("Tuple length:", len(my_tuple))

# 45) Concatenate two tuples
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# 46) Check if item exists in a tuple
if "hello" in my_tuple:
    print("Found")
else:
    print("Not found")

# 47) Create and print a set
my_set = {1, 2, 3}
print("Set:", my_set)

# 48) Check if element is in a set
print("Yes" if 2 in my_set else "No")

# 49) Add an element to a set
my_set.add(4)
print("After adding:", my_set)

# 50) Remove an element from a set
my_set.remove(1)
print("After removal:", my_set)

# 51) Union of two sets
set1 = {1, 2}
set2 = {2, 3}
print("Union:", set1 | set2)

# 52) Create and print a dictionary
person = {"name": "Alice", "age": 30}
print("Dictionary:", person)

# 53) Access value by key
print("Name:", person["name"])

# 54) Add key-value to dictionary
person["city"] = "New York"
print("Updated dictionary:", person)
