def square(x):
    return x * x

def apply_to_list(func, values):
    return [func(value) for value in values]

values = [1, 2, 3, 4, 5]
result = apply_to_list(square, values)
print(result)