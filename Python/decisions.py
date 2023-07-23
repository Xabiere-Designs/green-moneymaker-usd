import random

# Generate a random number between 0 and 10 (inclusive)
number = random.randint(0, 10)

thresh = 6

# Check if the number is greater than the threshold
if number > thresh:
    print('large number')
# Check if the number is less than 4
elif number < 4:
    print('really small number')
# Check if the number is less than 7
elif number < 7:
    print('small number')
# If none of the above conditions are met, the number must be 7
else:
    print('number is 7')

# Check if the number is greater than the threshold plus 1
if number > thresh + 1:
    print('really big number')

# Print the generated number
print(number)

