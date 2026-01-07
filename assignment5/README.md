# Assignment 5: Data Structures and Strings in Python

## Module 6: Data Structures and Strings in Python

This assignment contains two tasks focusing on Python data structures including dictionaries and lists, along with list slicing operations.

---

## 📌 Task 1: Create a Dictionary of Student Marks

### Description
A Python program that creates a dictionary of student names and their marks, allowing users to search for a specific student's marks.

### Features
- Creates a dictionary with student names as keys and marks as values
- Takes user input for student name
- Uses string methods (`strip()` and `capitalize()`) for input formatting
- Retrieves and displays marks for the entered student
- Handles cases where student is not found in the dictionary
- Uses a custom function `get_marks()` for lookup

### 🚀 How to Run
```bash
python task1.py
```

### Example Output

**If the student exists:**
```
Enter the student's name: anshu
Anshu's marks: 98.5
```

**If the student does not exist:**
```
Enter the student's name: John
Student not found.
```

---

## 📌 Task 2: Demonstrate List Slicing

### Description
A Python program that demonstrates list slicing operations by extracting elements and reversing them.

### Features
- Creates a list of numbers from 1 to 10
- Extracts the first five elements using list slicing
- Reverses the extracted elements using negative slicing
- Uses list slicing for operations
- Displays original, extracted, and reversed lists

### 🚀 How to Run
```bash
python task2.py
```

### Example Output
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted first five elements: [1, 2, 3, 4, 5]
Reversed extracted elements: [5, 4, 3, 2, 1]
```

---

## 💡 Learning Objectives
- Creating and manipulating dictionaries in Python
- Dictionary key-value pair access and lookup
- Using the `in` operator for membership testing
- String manipulation methods: `strip()` and `capitalize()`
- List slicing syntax and operations
- Negative indexing for reversing lists (`[::-1]`)
- Defining and calling custom functions
- Handling user input and formatting

## 📁 Files
- `task1.py` - Student marks dictionary lookup program
- `task2.py` - List slicing demonstration program
- `README.md` - This documentation file
