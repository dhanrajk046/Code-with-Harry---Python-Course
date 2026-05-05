# import os

# directory_path = "c:/"

# try:
#     entries = os.listdir(directory_path)
#     for entry in entries:
#         print(entry)
# except FileNotFoundError:
#     print("Directory not found")
# except PermissionError:
#     print("Permission denied")

import os

directory_path = "c:/"

try:
    entries = os.listdir(directory_path)
    for entry in entries:
        print(entry)
except FileNotFoundError:
    print("Directory not found")
except PermissionError:
    print("Permission denied")
