# OS Module -> Interacting with the Operating System
# Key Features:
# Operating System Interface: The OS mdule provides a way to interact with the underlying OS,
# whether it's windows, Linx, Mac OS
# File and Directory Operations: If offers functions for file and directory management, including creating,
# removing, and listing directories and files
# Current Working Directory: The module allows you to get and change the current working directory using
# functions like os.getcwd(), os.chdir()
# Platform Independence: The os module abstracts away platform-specific details, allowing you to write more
# portable code
import os

import os

print(os.getcwd())  # Returns current working directory

print(os.listdir('.'))

print(os.listdir('/Users/LENOVO/PycharmProjects_Test/PyATB5xLearning'))

# Create new directory
#os.mkdir('Test2')

#os.remove('Test2')

# Check if file exists
file_exist = os.path.exists("TestData.txt")
print(file_exist)   # True

file_exist = os.path.exists("TesttData.txt")
print(file_exist)   # False


print(os.name)   # nt