# import os

# # specify the directory path you want to list
# directory_path = "c:/"

# try:
#     # os.listdir() returns a list of all files and directories in the given path
#     entries = os.listdir(directory_path)

#     print(f"Contents of directory '{directory_path}':")
#     for entry in entries:
#         print(entry)

# except FileNotFoundError:
#     print(f"The directory '{directory_path}' does not exist.")
# except PermissionError:
#     print(f"Permission denied for accessing '{directory_path}'.")

#Using ChatGPT
import os

# Specify the directory path
path = "."   # "." means current directory

# Get list of files and directories
contents = os.listdir(path)

# Print each item
print("Contents of directory:")
for item in contents:
    print(item)