import os
import glob
import json

if os.name == 'nt':  # Check if the operating system is Windows
    slash = '\\'  # Set the slash character to backslash
else:
    slash = '/'  # Set the slash character to forward slash

files = []  # Initialize an empty list to store file information

for file in glob.glob(os.getcwd() + slash + '/*'):  # Iterate over files in the current directory

    file_dict = {'path':file.replace('\\','/'), 'size':os.path.getsize(file)}  # Create a dictionary with file path and size
    
    files.append(file_dict)  # Append the file dictionary to the files list
    
print(json.dumps(files, indent=4))  # Print the files list as JSON with indentation
