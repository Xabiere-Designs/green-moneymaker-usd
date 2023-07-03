import random
import uuid
import os

def generate_file(name = None, size = random.randint(3, 10)):
    if(name == None):  # Check if the name parameter is not provided
        name = str(uuid.uuid4())[:8] + '.dummy'  # Generate a random name using UUID if not provided
    with open(name, 'wb') as fout:  # Open the file in binary write mode
        fout.write(os.urandom(size))  # Write random bytes to the file
    fout.close()  # Close the file

