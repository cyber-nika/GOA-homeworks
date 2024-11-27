# 1. შედარება და ლოგიკური ოპერატორი (and)
a = 10
b = 5
c = 7
result = (a > b) and (a > c)  # True, რადგან a ორივე მნიშვნელობაზე დიდია
print(result)

# 2. შედარება და ლოგიკური ოპერატორი (or)
x = 15
y = 20
z = 10
result = (x < y) or (z > y)  # True, რადგან x პატარაა y-ზე
print(result)

# 3. შედარება და ლოგიკური ოპერატორი (and)
is_raining = True
has_umbrella = False
result = is_raining and has_umbrella  # False, რადგან umbrella არ გვაქვს
print(result)

# 4. შედარება და ლოგიკური ოპერატორი (or)
age = 30
is_adult = age >= 18
is_senior = age >= 60
result = is_adult or is_senior  # True, რადგან age >= 18
print(result)

# 5. შედარება და ლოგიკური ოპერატორი (and)
height = 175
weight = 70
is_healthy = (height >= 160) and (weight <= 75)  # True, ორივე პირობა erfüllt
print(is_healthy)

# 6. შედარება და ლოგიკური ოპერატორი (or)
a = 5
b = 10
c = 15
result = (a == b) or (b < c)  # True, რადგან b < c
print(result)

# 7. შედარება და ლოგიკური ოპერატორი (and)
num1 = 3
num2 = 6
num3 = 9
result = (num1 < num2) and (num2 < num3)  # True, რადგან num1 < num2 და num2 < num3
print(result)

# 8. შედარება და ლოგიკური ოპერატორი (or)
is_weekend = True
is_holiday = False
result = is_weekend or is_holiday  # True, რადგან is_weekend არის True
print(result)

# 9. შედარება და ლოგიკური ოპერატორი (and)
is_adult = True
is_student = False
result = is_adult and is_student  # False, რადგან is_student არის False
print(result)

# 10. შედარება და ლოგიკური ოპერატორი (or)
temperature = 25
is_sunny = True
is_hot = temperature > 30
result = is_sunny or is_hot  # True, რადგან is_sunny არის True
print(result)
