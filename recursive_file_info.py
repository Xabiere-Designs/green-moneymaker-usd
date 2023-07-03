import os
import glob
import json

def get_info(path='*'):
    if path == '*':  # Check if the path is the wildcard '*'
        path = os.getcwd()  # Set the path to the current working directory
    elif path[0] == '.':  # Check if the path starts with a dot '.'
        path = os.path.join(os.getcwd(), path)  # Construct the absolute path by joining the current working directory and the relative path

    if os.name == 'nt':  # Check if the operating system is Windows
        slash = '\\'  # Set the slash character to backslash
    else:
        slash = '/'  # Set the slash character to forward slash

    files_list = []  # Initialize an empty list to store file information

    for file in glob.glob(path + slash + '**', recursive=True):  # Iterate over files in the specified directory and its subdirectories
        file_size = os.path.getsize(file)  # Get the size of the file
        
        file_dict = {'path': file.replace('\\', '/'), 'size': file_size}  # Create a dictionary with file path and size
        
        files_list.append(file_dict)  # Append the file dictionary to the files list
        
    return files_list  # Return the list of file information

if __name__ == '__main__':
    files = get_info('..')  # Call the get_info function with a relative path
    print(json.dumps(files, indent=4))  # Print the files list as JSON with indentation

