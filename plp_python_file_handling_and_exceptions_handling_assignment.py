print("PLP_PYTHON_FILE_HANDLING_AND_EXCEPTIONS_HANDLING_ASSIGNMENT")

import os  # Importing the OS module to interact with the operating system (e.g., working with file paths)

# Opening and reading the content of the first text file
with open('not_useful/plp_file_handler1.txt') as file1:
    contents = file1.read()  # Reading the entire content of the file
    print(contents)  # Printing the contents to the console

print()  # Printing a blank line for better visual separation in the output

# Writing the contents from the first file into a new file (or overwriting if it exists)
with open('not_useful/plp_file_handler2.txt', 'w') as file2:
    for content in contents:  # Iterating over each character in the contents
        file2.write(f"{content}")  # Writing each character to the new file

# Appending new lines of text to the same file
with open('not_useful/plp_file_handler2.txt', 'a') as file2:
    file2.write("\nCurrently, I am learning Python Programming and loving the process.")
    file2.write("\nThis is great. I am grateful unto Power Learn Project for this opportunity.")

print()  # Printing another blank line for visual separation

# Setting up the path to search for a file in the "not_useful" directory
directory_path = r"C:\Users\youar\PycharmProjects\PythonProject5\not_useful"

# Asking the user to enter a filename (without extension)
filename_search = input("Enter the name of the file: ")

# Combining the directory path and the filename with the .txt extension
filename = os.path.join(directory_path, filename_search + ".txt")

# Checking if the specified file exists
if os.path.isfile(filename):
    with open(filename, 'r') as file:
        contents = file.read()  # Read the file's content
        print(contents)  # Display the contents
else:
    print("File not found")  # Message if the file does not exist
