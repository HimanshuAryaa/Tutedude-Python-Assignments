# Task 1: Perform Basic Mathematical Operations

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

addition = first_num + second_num
subtraction = first_num - second_num
multiplication = first_num * second_num

if second_num != 0:
    division = first_num / second_num
else:
    division= "Cannot divide by zero"

print("\nAddition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
