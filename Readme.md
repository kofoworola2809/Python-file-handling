# File Handling in Python

This project demonstrates how to **create, write, read, append, and handle exceptions** when working with files in Python.

---

## 📌 Features
1. **Creating and Writing to a File**  
   - Opens a file in write (`"w"`) mode.
   - Writes multiple lines of text to the file.

2. **Reading from a File**  
   - Opens a file in read (`"r"`) mode.
   - Reads and prints the file contents.

3. **Appending to a File**  
   - Opens a file in append (`"a"`) mode.
   - Adds new content without overwriting existing data.

4. **Exception Handling**  
   - Handles `FileNotFoundError` when a file doesn’t exist.
   - Catches and prints other unexpected errors.

---

## 📝 Example Code

```python
# Creating and writing to a new file
with open("New_file.txt", "w") as file:
    file.write("Hello, World!\\n")
    file.write("This is a new file created using Python.\\n")

# Reading from the file
with open("New_file.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to the existing file
with open("New_file.txt", "a") as file:
    file.write("This line is appended to the file.\\n")

# Exception Handling
try:
    with open("New_file.pdf", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
