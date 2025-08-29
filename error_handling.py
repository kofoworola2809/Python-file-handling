# Exception Handling
try:
    with open("New_file.pdf", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

    



