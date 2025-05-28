# Creating a single Python file content with solutions to all provided Codewars problems

solutions_code = """
# 1. Remove Unnecessary Characters
def remove_exclamation_marks(s):
    return s.replace('!', '')

# 2. Sum of all the multiples of 3 or 5
def find_multiples(n):
    return sum(x for x in range(1, n+1) if x % 3 == 0 or x % 5 == 0)

# 3. Count sheep
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n+1))

# 4. Name Shuffler
def name_shuffler(str_):
    return ' '.join(str_.split()[::-1])

# 5. Multiply two numbers
def multiply(a, b):
    return a * b

# 6. Fix string case
def solve(s):
    return s.lower() if sum(map(str.islower, s)) >= sum(map(str.isupper, s)) else s.upper()

# 7. Plural
def plural(n):
    return n != 1

# 8. Multiplication table for number
def multi_table(number):
    return '\\n'.join([f"{i} * {number} = {i*number}" for i in range(1, 11)])

# 9. Who is going to pay for the wall?
def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[:2]]

# 10. Default Arguments (fixing a bug)
def default_value(lst=None):
    if lst is None:
        lst = []
    lst.append("default")
    return lst

# 11. Convert to Binary
def to_binary(n):
    return int(bin(n)[2:])

# 12. Thinkful - Pixelart planning
def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0

# 13. Minimum Steps
def minimum_steps(numbers, value):
    numbers.sort()
    total, steps = 0, 0
    for num in numbers:
        total += num
        if total >= value:
            return steps
        steps += 1

# 14. Lightsabers
def how_many_light_sabers_do_you_own(name=''):
    return 18 if name == 'Zach' else 0

# 15. Stringy Strings
def stringy(size):
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(size)])

# 16. Without the letter 'e'
def sort_me(names):
    return sorted(names, key=lambda s: ('e' in s, s))

# 17. Shark Pontoon
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    return "Alive!" if pontoon_distance / you_speed < shark_distance / shark_speed else "Shark Bait!"

# 18. Worst Students
def worst_students(students):
    return sorted([s for s in students if s.endswith('?') or s.endswith('!')])

# 19. Reducing Problems
def tail_swap(strings):
    a, b = strings
    a1, a2 = a.split(':')
    b1, b2 = b.split(':')
    return [f"{a1}:{b2}", f"{b1}:{a2}"]

# 20. Christmas Tree Star
def starify(tree):
    return ['*' * len(row) for row in tree]

# 21. Trainers Meeting
def trainers_meetings(schedule):
    total = 0
    for row in zip(*schedule):
        if row.count(1) > 1:
            total += row.count(1)
    return total

# 22. Love vs Friendship
def words_to_marks(s):
    return sum(ord(c) - 96 for c in s)
"""

solutions_code
