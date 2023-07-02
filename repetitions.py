import random  # Importing the random module

numbers = list(range(10))


for number in numbers:
    print(number, number*2)  # Printing the number and its double

var2 = {'a':1, 'b':2, 'c':3}

for k, v in var2.items():
    print(k, v)  # Printing the key-value pairs of var2 dictionary

    for i in range(5):
        print('Green is the goat!')  # Printing the message "Green is the goat!" five times
        
number = random.randint(0, 100)  # Generating a random number between 0 and 100
counter = 0

while (number != 57):  # Loop until the generated number is 57
    number = random.randint(0, 100)  # Generating a new random number
    counter = counter + 1  # Incrementing the counter

print(counter, number)  # Printing the number of attempts and the final generated number


number = random.randint(0, 100)  # Generating a new random number
counter = 0

while (number != 57):  # Loop until the generated number is 57
    number = random.randint(0, 100)  # Generating a new random number
    counter = counter + 1  # Incrementing the counter
    if(counter >= 100):
        break  # Breaking the loop if the counter reaches 100

print(counter, number)  # Printing the number of attempts and the final generated number


number = random.randint(0, 100)  # Generating a new random number

for i in range(1000):
    if number == 57:
        break  # Breaking the loop if the generated number is 57
    number = random.randint(0, 100)  # Generating a new random number
    
print(i, number)  # Printing the number of iterations and the final generated number



