# grasshopper personalized message
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    return "Hello guest"

# car
def rental_car_cost(d):
    # your code
    cost = d * 40
    if d >= 7:
        cost  -= 50
    elif d >= 3 and d < 7:
        cost -=20
    return cost

# quarter of the year
def quarter_of(month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    
    quarters = {
        1: 1, 2: 1, 3: 1,
        4: 2, 5: 2, 6: 2,
        7: 3, 8: 3, 9: 3,
        10: 4, 11: 4, 12: 4
    }
    
    return quarters[month]

# remove exclamation mark
def remove_exclamation_marks(s):
    return s.replace('!', '')

# total amount of points 
def points(games):
    total_points = 0
    for game in games:
        score = game.split(':')
        if score[0] > score[1]:
            total_points += 3  # Win
        elif score[0] == score[1]:
            total_points += 1  # Draw
    return total_points

# jennys secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, " + name + "!"

# area or perimeter
def area_or_perimeter(length, width):
    if length == width:
        return length * width  # It's a square, return area
    else:
        return 2 * (length + width)  # It's a rectangle, return perimeter
    
# traffic lights
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"

# triangle third degree
def other_angle(angle1, angle2):
    return 180 - (angle1 + angle2)

# sum without highest or lowest number
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# messi goals 
# grasshopper personalized message
def greet(name, owner):
    if name == owner:
        return "Hello boss"
    return "Hello guest"

# car
def rental_car_cost(d):
    # your code
    cost = d * 40
    if d >= 7:
        cost  -= 50
    elif d >= 3 and d < 7:
        cost -=20
    return cost

# quarter of the year
def quarter_of(month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    
    quarters = {
        1: 1, 2: 1, 3: 1,
        4: 2, 5: 2, 6: 2,
        7: 3, 8: 3, 9: 3,
        10: 4, 11: 4, 12: 4
    }
    
    return quarters[month]

# remove exclamation mark
def remove_exclamation_marks(s):
    return s.replace('!', '')

# total amount of points 
def points(games):
    total_points = 0
    for game in games:
        score = game.split(':')
        if score[0] > score[1]:
            total_points += 3  # Win
        elif score[0] == score[1]:
            total_points += 1  # Draw
    return total_points

# jennys secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, " + name + "!"

# area or perimeter
def area_or_perimeter(length, width):
    if length == width:
        return length * width  # It's a square, return area
    else:
        return 2 * (length + width)  # It's a rectangle, return perimeter
    
# traffic lights
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"

# triangle third degree
def other_angle(angle1, angle2):
    return 180 - (angle1 + angle2)

# string repeat
def repeat_str(repeat, string):
    return string * repeat

# parse integer from string
def get_age(age):
    return int(age[0])

# greatest common divider
import math

def gcd(a, b):
    return math.gcd(a, b)

# Convert Number to Reversed Array of Digits
def digitize(n):
    return [int(d) for d in str(n)][::-1]

# check for even numbers
def check_for_factor(base, factor):
    return base % factor == 0
