import random
import uuid
import os

def generate_file(name: str = None, size: int = random.randint(1, 10)) -> None:
    if name is None:  # Check if the name parameter is not provided
        name = str(uuid.uuid4())[:8] + '.dummy'  # Generate a random name using UUID if not provided
    with open(name, 'wb') as fout:  # Open the file in binary write mode
        fout.write(os.urandom(size))  # Write random bytes to the file
    fout.close()  # Close the file

if __name__ == '__main__':
    for i in range(10):  # Loop 10 times
        generate_file()  # Generate a file with default parameters
