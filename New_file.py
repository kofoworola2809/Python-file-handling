# File Handling in Python
# This script demonstrates how to create, write, read, and append to a file in Python.

# # Creating and writing to a new file
with open("New_file.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new file created using Python.\n")
    
# Reading from the file
with open("New_file.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to the existing file
with open("New_file.txt", "a") as file:
    file.write("This line is appended to the file.\n")


 