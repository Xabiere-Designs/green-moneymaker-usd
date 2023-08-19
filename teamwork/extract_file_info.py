import os

def extract_file_info():
    file_list = []           # Initialize an empty list to store file information

    for filename in os.listdir():  # Iterate through items in the current directory
        if os.path.isfile(filename):  # Check if the item is a file
            file_info = {
                'name': filename,            # Create a dictionary entry for the file name
                'size': os.path.getsize(filename)  # Add the file size using os.path.getsize()
            }
            file_list.append(file_info)  # Append the file dictionary to the file_list

    return file_list   # Return the list containing file information dictionaries

if __name__ == '__main__':
    file_info_list = extract_file_info()   # Call the function to extract file information

    for file_info in file_info_list:      # Iterate through the list of file information dictionaries
        print(file_info)  # Print each dictionary containing file name and size

