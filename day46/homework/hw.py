# 2) Create a list comprehension that generates a list of numbers from 1 to 10.
numbers = [i for i in range(1, 11)]

# 3) Generate a list of squares of numbers from 1 to 5 using list comprehension.
squares = [i ** 2 for i in range(1, 6)]

# 4) Create a list of all even numbers between 1 and 20 using list comprehension.
evens = [i for i in range(1, 21) if i % 2 == 0]

# 5) Generate a list of the first letters of each word in a given list of words using list comprehension.
words = ['apple', 'banana', 'cherry', 'date']
first_letters = [word[0] for word in words]

# 6) Create a list comprehension that converts all words in a given list to uppercase.
uppercase_words = [word.upper() for word in words]

# 7) Create a list comprehension that generates a list of numbers from 1 to 50 that are divisible by 3.
divisible_by_3 = [i for i in range(1, 51) if i % 3 == 0]

# 8) Create a list comprehension that extracts words with more than 4 letters from a given list of words.
long_words = [word for word in words if len(word) > 4]

# 9) Create a list comprehension that converts a list of temperature values in Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

# 10) Create a list comprehension that finds all prime numbers between 1 and 100.
primes = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

# 11) Create a list comprehension that extracts all words from a given sentence that contain at least one vowel and are longer than 5 characters.
sentence = "This is an example sentence with several words"
vowels = "aeiou"
words = sentence.split()
long_words_with_vowels = [word for word in words if len(word) > 5 and any(vowel in word for vowel in vowels)]

# 12) Create a list comprehension that generates a sequence of Fibonacci numbers up to the 20th term.
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, 20)]

# Display all results
print("Numbers:", numbers)
print("Squares:", squares)
print("Evens:", evens)
print("First Letters:", first_letters)
print("Uppercase Words:", uppercase_words)
print("Divisible by 3:", divisible_by_3)
print("Long Words:", long_words)
print("Fahrenheit:", fahrenheit)
print("Primes:", primes)
print("Long Words with Vowels:", long_words_with_vowels)
print("Fibonacci:", fibonacci)
