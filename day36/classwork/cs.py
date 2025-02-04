def multiply(a, b):
    return a * b

#Even or Odd
def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else: return "Odd"

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversed Strings
def solution(string):
    return string[::-1]

#Return Negative
def make_negative( number ):
    if number > 0:
        return number * -1
    else: return number

#Opposite number
def opposite(number):
    return number * -1

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    if boolean==True:
        return "Yes"
    else:
        return "No"

#Sum of positive
def positive_sum(arr):
    res = 0
    for i in arr:
        if i > 0:
            res += i
    return res

#String repeat
def repeat_str(repeat, string):
    return string * repeat

#Remove First and Last Character
def remove_char(s):
    return s[1:-1]

#Square(n) Sum
def square_sum(numbers):
    result=0
    for i in numbers:
        result+=i**2
    return result