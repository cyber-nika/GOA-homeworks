# 1. Remove First and Last Character
def remove_char(s):
    # Removes the first and last character of the string
    return s[1:-1]


# 2. Reverse Words
def reverse_words(s):
    # Reverses each word in the string
    return ' '.join(word[::-1] for word in s.split())


# 3. Counting Duplicates
from collections import Counter

def duplicate_count(text):
    # Counts the number of characters that appear more than once, case-insensitive
    text = text.lower()
    return sum(1 for count in Counter(text).values() if count > 1)


# 4. Find the Smallest Integer in the Array
def find_smallest_int(arr):
    # Finds and returns the smallest integer in the array
    return min(arr)


# 5. Sum of Positive
def positive_sum(arr):
    # Sums only the positive numbers in the array
    return sum(x for x in arr if x > 0)


# 6. Get the Middle Character
def get_middle(s):
    # Returns the middle character(s) of the string
    length = len(s)
    return s[(length - 1) // 2: (length + 1) // 2]


# 7. Make a Function That Does Arithmetic
def arithmetic(a, b, operator):
    # Performs basic arithmetic operations based on the operator
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b


# 8. Convert a Number to a String
def number_to_string(num):
    # Converts the number to a string
    return str(num)


# 9. Remove the First and Last Character (Again)
def remove_char(s):
    # Removes the first and last character of the string
    return s[1:-1]


# 10. Century from Year
def what_century(year):
    # Returns the century of the given year
    return (year - 1) // 100 + 1


# 11. Is the Number Even or Odd?
def is_even_or_odd(n):
    # Determines if the number is even or odd
    return 'Even' if n % 2 == 0 else 'Odd'


# 12. Return a String of the First and Last Character
def make_new_string(s):
    # Returns a string consisting of the first and last character
    return s[0] + s[-1]


# 13. Reverse a String
def reverse_string(s):
    # Reverses the given string
    return s[::-1]


# 14. Basic Mathematical Operations
def basic_op(operator, value1, value2):
    # Performs basic mathematical operations
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2


# 15. Are You Playing Banjo?
def are_you_playing_banjo(name):
    # Returns "Yes" if the name starts with "R" or "r", else "No"
    return "Yes" if name.lower().startswith('r') else "No"


# 16. Convert Boolean to String
def boolean_to_string(b):
    # Converts boolean to string ("True" or "False")
    return str(b)


# 17. How Many Smallest Numbers
def count_smallest_numbers(arr):
    # Counts how many times the smallest number appears in the array
    smallest = min(arr)
    return arr.count(smallest)