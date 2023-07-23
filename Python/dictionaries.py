import random  # Importing the random module

var = {}

print(type(var))  # Inline comment: Printing the type of var

var2 = {'color': 'blue', 'juice': 'cranberry', 'fruit': 'mango'}

print(var2)  # Inline comment: Printing the var2 dictionary

var2['drink'] = 'jose'

print(var2)  # Inline comment: Printing the updated var2 dictionary

var2['fruit'] = 'apple'

print(var2)  # Inline comment: Printing the updated var2 dictionary

del var2['fruit']

print(var2)  # Inline comment: Printing the updated var2 dictionary

print(var2['drink'])  # Inline comment: Printing the value corresponding to the 'drink' key in var2

var2['fruit'] = 'mango'

print(var2)  # Inline comment: Printing the updated var2 dictionary

print(dir(var2))  # Inline comment: Printing the list of available attributes and methods of var2

print(var2.keys())  # Inline comment: Printing the keys of var2

print(var2.values())  # Inline comment: Printing the values of var2

print(var2.items())  # Inline comment: Printing the key-value pairs of var2

for k, v in var2.items():
    print(k, v)  # Inline comment: Printing each key-value pair of var2

var3 = {j: [random.randint(0, 100) for i in range(5)] for j in range(5)}

print(var3)  # Inline comment: Printing the var3 dictionary
