# 1. Find the missing letter
def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i]) + 1 != ord(chars[i + 1]):
            return chr(ord(chars[i]) + 1)

# 2. Basic mathematical operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

# 3. Smallest integer in the array
def find_smallest_int(arr):
    return min(arr)

# 4. Vowel Count
def getCount(string):
    return sum(1 for char in string if char in 'aeiouAEIOU')

# 5. Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# 6. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

# 7. Sum of positive
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 8. Remove Duplicates
def remove_duplicates(numbers):
    return list(set(numbers))

# 9. Find the missing letter
def findMissingLetter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i]) + 1 != ord(chars[i + 1]):
            return chr(ord(chars[i]) + 1)

# 10. Convert a string to a number
def string_to_number(s):
    return int(s)

# 11. Counting duplicates
def duplicate_count(text):
    counts = {}
    duplicates = 0
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    for count in counts.values():
        if count > 1:
            duplicates += 1
    return duplicates

# 12. Return the sum of two smallest integers
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# 13. Find the divisors
def divisors(integer):
    divisors_list = []
    for i in range(2, integer):
        if integer % i == 0:
            divisors_list.append(i)
    return divisors_list if divisors_list else f"{integer} is prime"

# 14. Generate range of integers
def between(a, b):
    return list(range(a, b + 1))

# 15. Reverse a string
def solution(string):
    return string[::-1]

# 16. Find the odd numbers
def is_odd(n):
    return n % 2 != 0

# 17. Sum of all positive numbers
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 18. Count the total number of digits
def digits(n):
    return len(str(abs(n)))

# 19. Find the next perfect square
def find_next_square(n):
    root = n ** 0.5
    return (root + 1) ** 2 if root.is_integer() else -1

# 20. Convert a boolean to a string
def boolean_to_string(b):
    return "true" if b else "false"

# 21. Multiply the sum of elements by the count
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]

# 22. Check if string contains vowels
def is_vow(string):
    return any(char in "aeiouAEIOU" for char in string)

# 23. Return the reversed number
def reverse_number(n):
    return int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)

# 24. Count how many people like a post
def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return f"{names[0]} likes this"
    elif n == 2:
        return f"{names[0]} and {names[1]} like this"
    elif n == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {n - 2} others like this"

# 25. Check if string contains only lowercase letters
def is_lower_case(s):
    return s.islower()

# 26. Find the maximum number in an array
def find_max(arr):
    return max(arr)

# 27. Validate if number is even
def is_even(n):
    return n % 2 == 0

# 28. Return an array with n repetitions of a number
def repeat_it(string, n):
    return [string] * n
