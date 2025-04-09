# Get the mean of an array
def get_average(marks):
    raise NotImplementedError("TODO: get_average")
def get_average(marks):
    return int(sum(marks) / len(marks))


# Keep up the hoop
def hoop_count(n):
    if n < 10: return "Keep at it until you get it"
    return "Great, now move on to tricks"


# Reversed Words
def reverse_words(s):
    return " ".join(s.split(' ')[::-1])



# Beginner Series #4 Cockroach
def cockroach_speed(s):
    return int(s*27.777778)



# squaring an argument
def switch_it_up(number):
    res = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return res[number]



    # Removing Elements
def remove_every_other(my_list):
    return my_list[::2]



# 2nd variation
def remove_every_other(my_list):
    new_list = []

    for i in range(len(my_list)):
        if i%2 == 0: new_list.append(my_list[i])

    return new_list




# Twice as old
def twice_as_old(dad_years_old, son_years_old):
    res = (dad_years_old - 2 * son_years_old)

    if res < 0: return res-1
    return res




# All Star Code Challenge #18
def str_count(strng, letter):
    return strng.count(letter)



# Is it even?
def is_even(n): 
    return n % 2 == 0



# Grasshopper - Terminal game move function
def move(position, roll):
    return position + roll



# get planet name by ID codewars
def get_planet_name(id: int) -> str:
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planets.get(id, "Invalid ID")



# will there be enough space
def enough(cap: int, on: int, wait: int) -> int:
    return max(0, on + wait - cap)



# what is between
def between(a: int, b: int) -> list:
    return list(range(a, b + 1))


# is the string uppercase 
def is_uppercase(inp):
    return inp.isupper()