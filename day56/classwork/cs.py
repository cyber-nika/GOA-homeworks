# 1. Return the maximum value by trying different combinations of + and *
def expression_matter(a, b, c):
    return max(a + b + c, a * b * c, (a + b) * c, a * (b + c))


# 2. Reverse the array to fix the meerkat's head and tail
def fix_the_meerkat(arr):
    return arr[::-1]


# 3. Check whether the number is even or odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# 4. Count how many odd numbers are below a given number
def odd_count(n):
    return n // 2


# 5. Return a message depending on whether the name starts with 'R'
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"


# 6. Check if a string is entirely uppercase
def is_uppercase(inp):
    return inp == inp.upper()


# 7. Check if one number is a factor of another
def check_for_factor(base, factor):
    return base % factor == 0


# 8. Remove all digits from a string
def string_clean(s):
    return ''.join(filter(lambda x: not x.isdigit(), s))


# 9. Mutate a string step-by-step until it matches the target string
def mutate_my_strings(string1, string2):
    result = [string1]
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            string1 = string1[:i] + string2[i] + string1[i+1:]
            result.append(string1)
    return '\n'.join(result) + '\n'


# 10. Perform a basic arithmetic operation based on the given operator
def basic_op(operator, value1, value2):
    return eval(f"{value1}{operator}{value2}")


# 11. Return a simple greeting with the person's name
def greet(name): 
    return f"Hello, {name}!"


# 12. Return a list of all multiples of a number up to a given limit
def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1, integer)]


# 13. Add each word's length next to it in a list
def add_length(s):
    return [f"{word} {len(word)}" for word in s.split()]
