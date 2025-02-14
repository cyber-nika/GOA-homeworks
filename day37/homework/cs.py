my_tuple = (10, 20, 30, 40, 50)
second_element = my_tuple[1]
last_element = my_tuple[-1]
middle_slice = my_tuple[1:4]
print(f"Second Element: {second_element}, Last Element: {last_element}, Middle Slice: {middle_slice}")

try:
    my_tuple[1] = 99
except TypeError as e:
    print(f"Tuple Immutability Error: {e}")

packed_tuple = ("Alice", 25, "Developer")
name, age, job = packed_tuple 
print(f"Name: {name}, Age: {age}, Job: {job}")

repeated_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = repeated_tuple.count(2)
index_of_3 = repeated_tuple.index(3)
print(f"Count of 2: {count_of_2}, Index of 3: {index_of_3}")

my_set = {10, 20, 30, 40, 50}
my_set.add(60)
my_set.remove(30) 
print(f"Updated Set: {my_set}, Is 40 in set? {'Yes' if 40 in my_set else 'No'}")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
union_set = set_a | set_b 
intersection_set = set_a & set_b 
difference_set = set_a - set_b 
print(f"Union: {union_set}, Intersection: {intersection_set}, Difference: {difference_set}")

duplicate_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_set = set(duplicate_list) 
unique_list = list(unique_set) 
print(f"List without duplicates: {unique_list}")
