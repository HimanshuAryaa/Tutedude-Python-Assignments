# Assignment 6: Calculator Using Tkinter

## Module 14 & 15: Calculator Using Tkinter

This assignment is a GUI-based calculator application built using Python's Tkinter library. The calculator performs basic arithmetic operations with a clean, user-friendly interface.

---

## 📌 Project Overview

### Description
A fully functional desktop calculator application with a graphical user interface that performs basic mathematical operations including addition, subtraction, multiplication, and division.

### Features
- ✨ Clean and intuitive GUI design
- 🔢 Number buttons (0-9) for input
- ➕ Basic arithmetic operations: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- 🧹 Clear button (⌫) to reset the calculator
- ⚠️ Error handling for division by zero
- 🎨 Dark-themed interface with custom colors
- 🔒 Keyboard input protection to prevent invalid entries
- 📱 Compact window size (310x300 pixels)

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your system
- Tkinter library (usually comes pre-installed with Python)

### Running the Calculator
```bash
python calculator.py
```

---

## 💻 Usage Instructions

1. **Launch the application** by running the Python file
2. **Click number buttons** to enter numbers
3. **Click operation buttons** (+, -, *, /) to select an operation
4. **Click the equals button (=)** to calculate the result
5. **Click the clear button (⌫)** to reset and start a new calculation

### Example Calculation
```
Enter: 15
Click: +
Enter: 25
Click: =
Result: 40
```

---

## 📸 Screenshots

### Calculator Initial State
![Calculator Initial State](assignment6-tkinter-calculator/screenshots/calculator_initial.png)

*The calculator interface on startup with default '0' display*

---

### Calculator in Action
![Calculator Performing Operation](assignment6-tkinter-calculator/screenshots/calculator_operation.png)

*Example showing a calculation being performed (58 displayed)*

---

### Error Handling Demo
![Division by Zero Error](assignment6-tkinter-calculator/screenshots/calculator_error.png)

*Error message displayed when attempting to divide by zero*

---

## 🛠️ Technical Details

### Technologies Used
- **Python 3.x**
- **Tkinter** - GUI framework

### Key Components
- **Entry Widget**: Display box for showing input and results
- **Button Widgets**: Interactive buttons for numbers and operations
- **Event Handling**: Lambda functions for button click events
- **Error Handling**: Try-except blocks for division by zero

---

## 🎯 Learning Objectives

- Creating GUI applications with Tkinter
- Using widgets: Entry, Button, and window configuration
- Event handling with lambda functions and command parameters
- Global variables for state management
- Error handling in GUI applications
- Layout management using `.place()` method
- String manipulation and type conversion
- User input validation and protection

---

## 🐛 Error Handling

The calculator includes robust error handling:
- **Division by Zero**: Displays "Can't divide by zero" message
- **Invalid Input Protection**: Keyboard input is disabled to prevent invalid entries
- **State Reset**: Clear button resets all states and displays

---

## 🔮 Future Enhancements

Possible improvements for the calculator:
- Add decimal point support for floating-point calculations
- Implement percentage calculations
- Add keyboard shortcuts for operations
- Include memory functions (M+, M-, MR, MC)
- Add calculation history
- Implement scientific calculator functions
- Add backspace functionality for single digit deletion

---

## 💡 Learning Objectives
- Creating GUI applications with Tkinter
- Widget configuration and placement
- Event-driven programming with lambda functions
- State management using global variables
- Exception handling in GUI context
- User input validation and error prevention
- Layout management techniques

## 📁 Files
- `src/` - Folder containing sorce code file 
  - `calculator.py` - Main calculator application file
- `README.md` - This documentation file
- `screenshots/` - Folder containing application screenshots
  - `calculator_initial.png` - Calculator default state
  - `calculator_operation.png` - Calculator during operation
  - `calculator_error.png` - Error handling demonstration

---

## 👤 Author

[Himanshu Arya]
Created as part of the TuteDude Python Programming Course - Module 14 & 15

---

## 📄 License

This project is for educational purposes as part of the TuteDude Python course.
