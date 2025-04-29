# 1) Lambda function that adds 5 to a given number
add_five = lambda x: x + 5
print(add_five(10))  # Output: 15

# 2) Lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# 3) Lambda function to check if a number is even
is_even = lambda x: x % 2 == 0
print(is_even(10))  # Output: True
print(is_even(7))   # Output: False

# 4) Lambda function to convert a list of temperatures from Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
temperatures_in_celsius = [0, 20, 37, 100]
temperatures_in_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_in_celsius))
print(temperatures_in_fahrenheit)  # Output: [32.0, 68.0, 98.6, 212.0]

# 5) Lambda function that returns True if a string starts with the letter 'A'
starts_with_a = lambda s: s[0].lower() == 'a'
print(starts_with_a("Apple"))  # Output: True
print(starts_with_a("Banana")) # Output: False

# ---- Using map() for different operations ----

# 6) Use map() to add 10 to every number in a list
numbers = [1, 2, 3, 4, 5]
add_ten = lambda x: x + 10
result = list(map(add_ten, numbers))
print(result)  # Output: [11, 12, 13, 14, 15]

# 7) Use map() to convert a list of strings to uppercase
strings = ["hello", "world", "python"]
to_uppercase = lambda x: x.upper()
uppercase_strings = list(map(to_uppercase, strings))
print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# 8) Use map() to find the length of each word in a list of strings
words = ["apple", "banana", "cherry"]
word_lengths = lambda x: len(x)
lengths = list(map(word_lengths, words))
print(lengths)  # Output: [5, 6, 6]

# 9) Use map() to square each number in a list
numbers = [1, 2, 3, 4]
square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]

# 10) Use map() to convert a list of integers to strings
numbers = [1, 2, 3, 4]
to_string = lambda x: str(x)
string_numbers = list(map(to_string, numbers))
print(string_numbers)  # Output: ['1', '2', '3', '4']

# 11) Use map() to concatenate the string "Hello " to each name in a list of names
names = ["Alice", "Bob", "Charlie"]
add_hello = lambda name: "Hello " + name
greeted_names = list(map(add_hello, names))
print(greeted_names)  # Output: ['Hello Alice', 'Hello Bob', 'Hello Charlie']

# 12) Use map() to subtract 5 from every element in a list
numbers = [10, 20, 30, 40]
subtract_five = lambda x: x - 5
result = list(map(subtract_five, numbers))
print(result)  # Output: [5, 15, 25, 35]

# 13) Use map() to multiply each number in a list by 3
numbers = [1, 2, 3, 4]
multiply_by_three = lambda x: x * 3
result = list(map(multiply_by_three, numbers))
print(result)  # Output: [3, 6, 9, 12]

# 14) Use map() to convert a list of temperatures in Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
fahrenheit = list(map(celsius_to_fahrenheit, celsius))
print(fahrenheit)  # Output: [32.0, 68.0, 98.6, 212.0]

# 15) Use map() to check if numbers in a list are greater than 50
numbers = [10, 60, 30, 80]
greater_than_50 = lambda x: x > 50
result = list(map(greater_than_50, numbers))
print(result)  # Output: [False, True, False, True]

# ---- Using filter() for different operations ----

# 16) Use filter() to keep only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# 17) Use filter() to select numbers greater than 10 from a list
numbers = [5, 12, 8, 25, 3]
greater_than_10 = lambda x: x > 10
numbers_above_10 = list(filter(greater_than_10, numbers))
print(numbers_above_10)  # Output: [12, 25]

# 18) Use filter() to keep strings longer than 5 characters from a list of strings
strings = ["apple", "banana", "kiwi", "cherry"]
long_strings = lambda x: len(x) > 5
long_strings_list = list(filter(long_strings, strings))
print(long_strings_list)  # Output: ['banana', 'cherry']

# 19) Use filter() to remove empty strings from a list of strings
strings = ["apple", "", "banana", "cherry", ""]
non_empty_strings = lambda x: x != ""
non_empty_list = list(filter(non_empty_strings, strings))
print(non_empty_list)  # Output: ['apple', 'banana', 'cherry']

# 20) Use filter() to select only positive numbers from a list
numbers = [-10, 20, 30, -5, 50]
positive_numbers = lambda x: x > 0
positive_list = list(filter(positive_numbers, numbers))
print(positive_list)  # Output: [20, 30, 50]

# 21) Use filter() to keep names that start with the letter 'A' from a list of names
names = ["Alice", "Bob", "Anna", "Charlie"]
starts_with_a = lambda x: x[0].lower() == 'a'
names_starting_with_a = list(filter(starts_with_a, names))
print(names_starting_with_a)  # Output: ['Alice', 'Anna']

# 22) Use filter() to get numbers divisible by 3 from a list
numbers = [3, 5, 6, 9, 10]
divisible_by_3 = lambda x: x % 3 == 0
divisible_by_3_list = list(filter(divisible_by_3, numbers))
print(divisible_by_3_list)  # Output: [3, 6, 9]

# 23) Use filter() to keep words that contain the letter 'e' from a list of words
words = ["apple", "banana", "cherry", "date"]
contains_e = lambda x: 'e' in x
words_with_e = list(filter(contains_e, words))
print(words_with_e)  # Output: ['apple', 'cherry', 'date']

# 24) Use filter() to remove all None values from a list
values = [1, None, 3, None, 5]
no_none = lambda x: x is not None
filtered_values = list(filter(no_none, values))
print(filtered_values)  # Output: [1, 3, 5]

# 25) Use filter() to keep numbers that are less than or equal to 50 from a list
numbers = [10, 60, 30, 50, 70]
less_than_or_equal_50 = lambda x: x <= 50
numbers_up_to_50 = list(filter(less_than_or_equal_50, numbers))
print(numbers_up_to_50)  # Output: [10, 30, 50]
