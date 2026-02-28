# Task 2: Write and Append Data to a File

try:
    with open("output.txt", 'a') as f:
        f.write(input("Enter text to write to the file: ") + "\n")
        print("Data successfully written to output.txt\n")

        f.write(input("Enter additional text to append: ") + "\n")
        print("Data successfully appended.\n")

    with open("output.txt", 'r') as f:
        data = f.read()
        print("Final content of output.txt:")
        print(data.rstrip())
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")
