# Task 2: Convert a sentence to uppercase
sentence = input("Enter a sentence: ")
print(sentence.upper())

# Task 3: Display a user's name in uppercase
name = input("Enter your name: ")
print(name.upper())

# Task 4: Convert a list of lowercase strings to uppercase
def convert_to_uppercase(strings):
    return [s.upper() for s in strings]
print(convert_to_uppercase(["hello", "world", "python"]))

# Task 5: Convert a sentence to lowercase
sentence = input("Enter a sentence: ")
print(sentence.lower())

# Task 6: Store email in lowercase
email = input("Enter your email address: ")
email = email.lower()
print(f"Stored email: {email}")

# Task 7: Convert a mixed-case string to lowercase
def to_lowercase(mixed_string):
    return mixed_string.lower()
print(to_lowercase("Hello, World!"))

# Task 8: Capitalize the first letter of a sentence
sentence = input("Enter a sentence: ")
print(sentence.capitalize())

# Task 9: Capitalize the first letter of each string in a list
def capitalize_list(strings):
    return [s.capitalize() for s in strings]
print(capitalize_list(["hello", "world", "python"]))

# Task 10: Capitalize the first letter of a string
def capitalize_first(s):
    return s.capitalize()
print(capitalize_first("python is amazing!"))

# Task 11: Find the position of "Python" in a sentence
sentence = input("Enter a sentence: ")
print(sentence.find("Python"))

# Task 12: Find the starting index of a substring
sentence = input("Enter a string: ")
substring = input("Enter the substring to search: ")
print(sentence.find(substring))

# Task 13: Find the index of a character in a string
def find_character(string, char):
    return string.find(char)
print(find_character("hello", "e"))

# Task 14: Find and print the length of a string
string = input("Enter a string: ")
print(len(string))

# Task 15: Return the lengths of strings in a list
def get_lengths(strings):
    return [len(s) for s in strings]
print(get_lengths(["hello", "world", "python"]))

# Task 16: Count occurrences of "the" in a paragraph
paragraph = input("Enter a paragraph: ")
print(paragraph.lower().count("the"))

# Task 17: Count occurrences of a character
string = input("Enter a string: ")
char = input("Enter a character: ")
print(string.count(char))

# Task 18: Count occurrences of a word in text
def count_word(text, word):
    return text.lower().count(word.lower())
print(count_word("The quick brown fox jumps over the lazy dog.", "the"))

# Task 19: Find index of "hello"
string = input("Enter a string: ")
print(string.find("hello"))

# Task 20: Find index of a character
def find_char(string, char):
    return string.find(char)
print(find_char("hello world", "o"))

# Task 21: Check if a string is lowercase
string = input("Enter a string: ")
print(string.islower())

# Task 22: Function to check if string is lowercase
def is_all_lowercase(string):
    return string.islower()
print(is_all_lowercase("hello"))

# Task 23: Verify if input is lowercase
string = input("Enter a string: ")
if string.islower():
    print("The string is in lowercase.")
else:
    print("The string is not in lowercase.")

# Task 24: Verify if a string is uppercase
string = input("Enter a string: ")
print(string.isupper())

# Task 25: Function to check if a string is uppercase
def is_all_uppercase(string):
    return string.isupper()
print(is_all_uppercase("HELLO"))

# Task 26: Check if user input is uppercase
string = input("Enter a string: ")
if string.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")

# Task 27: Replace "dog" with "cat"
sentence = input("Enter a sentence: ")
print(sentence.replace("dog", "cat"))

# Task 28: Replace spaces with underscores
def replace_spaces(string):
    return string.replace(" ", "_")
print(replace_spaces("hello world python"))

# Task 29: Swapcase of a string
string = input("Enter a string: ")
print(string.swapcase())

# Task 30: Function to swapcase
def swap_case(string):
    return string.swapcase()
print(swap_case("Hello World!"))
