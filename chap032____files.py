"""
Python Working with Files
In Python, working with files is an essential operation for reading and writing data. Python provides built-in functions
and methods to handle files efficiently. Here's a comprehensive guide to working with files in Python.
1. Opening a File
To interact with a file, the first step is to open it using the open() function.
"""
file = open("example.txt", "r")  # Open file in read mode ('r')
"""
File Modes:
'r': Read (default mode). Opens the file for reading.
'w': Write. Opens the file for writing (creates a new file or truncates an existing file).
'a': Append. Opens the file for appending (creates a new file if it doesn't exist).
'b': Binary. Reads or writes the file in binary mode (e.g., 'rb' for reading binary files).
'x': Exclusive creation. Creates a new file, and if it already exists, it raises an error.
2. Reading from a File
Reading Entire File
"""
# Open file in read mode
file = open("example.txt", "r")
# Read the entire content of the file
content = file.read()
print(content)
# Close the file
file.close()
# Open file in read mode
file = open("example.txt", "r")
# Read the file line by line
for line in file:
    print(line.strip())  # strip() removes the trailing newline character

file.close()
# Reading Specific Number of Characters
file = open("example.txt", "r")
# Read first 5 characters
content = file.read(5)
print(content)

file.close()
# 3. Writing to a File

# Open file in write mode
file = open("example.txt", "w")

# Write some content to the file
file.write("Hello, World!\nWelcome to Python.")

# Close the file
file.close()
# Appending to a File
# Open file in append mode
file = open("example.txt", "a")

# Append some content to the file
file.write("\nAppended text.")

# Close the file
file.close()
"""
4. Working with Context Manager (with statement)
Using the with statement ensures that the file is properly closed after the block of code is executed, even if an 
exception occurs.

Example: Using with to Open a File
"""
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# No need to explicitly call file.close(), it's done automatically
# Writing with Context Manager
with open("example.txt", "w") as file:
    file.write("This is a new content written to the file.")
"""    
5. File Operations
Checking if File Exists
"""
import os

# Check if the file exists
if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File does not exist!")
# Getting File Information

import os
# Get file size
file_size = os.path.getsize("example.txt")
print(f"File size: {file_size} bytes")

# Get the file's last modification time
mod_time = os.path.getmtime("example.txt")
print(f"Last modified: {mod_time}")
# Renaming a File

import os
# Rename a file
os.rename("example.txt", "renamed_example.txt")
# Deleting a File

import os
# Remove the file
os.remove("renamed_example.txt")
# 6. File Paths
# Example: Using Absolute and Relative Paths
# Using a relative path
with open("folder/example.txt", "r") as file:
    content = file.read()
    print(content)

# Using an absolute path
with open("/home/user/example.txt", "r") as file:
    content = file.read()
    print(content)
# 7. Binary Files
# For working with binary data, you can use 'b' mode.
# Example: Reading a Binary File

with open("image.jpg", "rb") as file:
    binary_data = file.read()
    print(binary_data)  # Prints binary data of the file
# Example: Writing to a Binary File

with open("output.jpg", "wb") as file:
    file.write(binary_data)  # Writes the binary data to a new file
# 8. File Handling Errors
# It's good practice to handle errors that may occur during file operations, such as file not found or permission issues.

# Example: Handling File Errors

try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist!")
except IOError:
    print("An error occurred while handling the file!")
"""    
9. Working with CSV Files
You can use the csv module to read from and write to CSV files.
"""
# Reading a CSV File

import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Writing to a CSV File

import csv
data = [["Name", "Age", "City"], ["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"]]
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
# 10. Working with JSON Files
# The json module allows you to work with JSON data stored in files.

# Reading from a JSON File

import json
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
# Writing to a JSON File

import json
data = {"name": "Alice", "age": 25, "city": "New York"}
with open("output.json", "w") as file:
    json.dump(data, file)
"""
Summary
Key File Operations:
Opening: open()
Reading: read(), readline(), readlines()
Writing: write(), writelines()
Closing: close() (or using with to automatically close)
Appending: 'a' mode
File handling: os.path.exists(), os.rename(), os.remove()
Error handling: try-except
CSV and JSON: Using csv and json modules for structured data
Using Python's file handling functions, you can easily manage files for reading, writing, and organizing data.
"""
