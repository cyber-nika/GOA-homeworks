data = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2022,
    "color": "Red",
    "autopilot": True
}

print(data.keys())
print(data.values())
print(data.items())

for key, value in data.items():
    print(f"{key}: {value}")
