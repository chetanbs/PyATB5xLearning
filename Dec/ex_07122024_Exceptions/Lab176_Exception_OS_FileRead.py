# Read the file
# File reading is a fundamental operation in Python that allows you to access and manipulate
# data stored in text file
# file.open(("path or name of the file"),"mode")
# path or name of the file ->
# mode -> r, w, x -> r - read, w- write, x - execute
# mode -> r, w, x,a,b,t,+

import os

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path + "/example.txt"
    print(full_path_file)
    # Read the file
    file = open(full_path_file)
except Exception as fnfe:
    print("File not found, fix the path or create a file")
finally:
    print("This finally part execute always")

