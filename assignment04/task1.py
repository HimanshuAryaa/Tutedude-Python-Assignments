# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", 'r') as f:
        content = f.readlines()
        if len(content) == 0:
            raise IndexError
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except IndexError:
    print("Error: The file 'sample.txt' is empty.")
else:
    print("Reading file content:")
    for line in range(len(content)):
        print(f"Line {line + 1}: {content[line].rstrip()}")
