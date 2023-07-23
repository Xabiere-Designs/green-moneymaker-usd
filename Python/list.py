import random

var = []

print(type(var))  # Print the type of the variable 'var'

var2 = [151, 253, 306, 403, "009"]

print(var2)  # Print the contents of the list 'var2'

var2.append(640)  # Add the value 640 to the end of the list 'var2'

print(var2)  # Print the updated contents of 'var2'

var2.reverse()  # Reverse the order of elements in 'var2'

print(var2)  # Print the reversed list 'var2'

print(dir(var2))  # Print the list of available methods for 'var2'

var3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(var3)  # Print the contents of the list 'var3'

numbers = list(range(15))  # Create a list of numbers from 0 to 14

print(numbers)  # Print the numbers list

print(numbers[5])  # Print the value at index 5 of the numbers list

print(len(numbers))  # Print the length of the numbers list

for number in numbers:
    print(number, number * 2)  # Print each number and its double in the numbers list

var4 = [[random.randint(0, 100) for i in range(5)] for i in range(5)]

print(var4)  # Print the 5x5 matrix of random numbers between 0 and 100

    
    
    








