import os
import glob
import json

def get_info(path=os.getcwd()):
    if path[0] == '.':  # Check if the path starts with a dot '.'
        path = os.path.join(os.getcwd(), path)  # Construct the absolute path by joining the current working directory and the relative path

    files_dict = {'path': path.replace('\\', '/')}  # Create a dictionary with the root path

    files_dict['files'], files_dict['size'] = get_info_recursive(path)  # Call get_info_recursive to get file information recursively

    return files_dict


def get_info_recursive(path):
    if os.name == 'nt':  # Check if the operating system is Windows
        slash = '\\'  # Set the slash character to backslash
    else:
        slash = '/'  # Set the slash character to forward slash

    files_list = []  # Initialize an empty list to store file information

    for file in glob.glob(path + slash + '/**', recursive=False):  # Iterate over files in the current directory
        file_dict = {'path': file.replace('\\', '/'), 'size': os.path.getsize(file)}  # Create a dictionary with file path and size
        files_list.append(file_dict)  # Append the file dictionary to the files list

    total_size = sum([f['size'] for f in files_list])  # Calculate the total size of all files

    files_dict = {os.path.basename(path): {'path': path.replace('\\', '/'), 'size': total_size, 'files': {}}}  # Create a dictionary for the current directory

    for file_dict in files_list:
        dir_path = os.path.dirname(file_dict['path'])
        file_name = os.path.basename(file_dict['path'])
        dir_dict = files_dict
        for dir_name in os.path.relpath(dir_path, path).split(os.sep):  # Iterate over the relative path components
            if dir_name:
                dir_dict = dir_dict[file_name]['files'].setdefault(dir_name, {'path': os.path.join(path, dir_name).replace('\\', '/'), 'size': 0, 'files': {}})
                # Create a subdirectory dictionary if it doesn't exist, with initial size and files as 0
            else:
                dir_dict = dir_dict[file_name]['files']  # Move to the next level of the directory structure

        dir_dict[file_name] = file_dict  # Add the file dictionary to the directory dictionary

    return files_dict[os.path.basename(path)], total_size


if __name__ == '__main__':
    files = get_info('..')  # Call the get_info function with a relative path
    print(json.dumps(files, indent=4))  # Print the files list as JSON with indentation

