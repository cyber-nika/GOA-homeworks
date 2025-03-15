# 2) Dictionary Explanation
# Dictionary is a data structure that stores key-value pairs.
# Unlike lists, dictionaries allow access to values using unique keys instead of index positions.

# 3) Print all keys using keys()
my_dict = {"name": "Ana", "age": 25, "city": "Tbilisi", "job": "Developer", "hobby": "Reading"}
print(my_dict.keys())

# 4) Print all values using values()
print(my_dict.values())

# 5) Print all key-value pairs using items()
print(my_dict.items())

# 6) Iterate over dictionary using items()
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 7) Check if a specific key exists using in
if "age" in my_dict:
    print("Key exists")
else:
    print("Key does not exist")

# 8) Retrieve a value using get() with error handling
age = my_dict.get("age", "Not Found")
print(age)

salary = my_dict.get("salary", "Not Found")
print(salary)

# 9) Add a new key-value pair and print updated dictionary
my_dict["country"] = "Georgia"
print(my_dict)

# 10) Remove a key-value pair using pop()
my_dict.pop("age")
print(my_dict)

# 11) Update dictionary using update()
new_data = {"city": "Tbilisi", "job": "Developer"}
my_dict.update(new_data)
print(my_dict)

# 12) Print the length of dictionary
print(len(my_dict))

# 13) Function to sum all numeric values
def sum_numeric_values(dictionary):
    return sum(value for value in dictionary.values() if isinstance(value, (int, float)))

data = {"a": 10, "b": 20, "c": "hello", "d": 5.5}
print(sum_numeric_values(data))  # Output: 35.5

# 14) Clear all elements using clear()
my_dict.clear()
print(my_dict)  # Output: {}

# 15) Personal Dictionary
my_info = {
    "name": "Nika ",
    "surname": "Chubunidze ",
    "age": 15,
    "city": "Tbilisi",
    "country": "Georgia",
    "job": "graphic designer ",
    "company": "Tech corp ",
    "hobby": "Gym ",
    "favorite_food": "Khinkali",
    "pet": "Dog"
}
print(my_info)
