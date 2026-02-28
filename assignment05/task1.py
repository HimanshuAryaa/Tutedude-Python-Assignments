 Task 1: Create a Dictionary of Student Marks

students_marks = {"Anshu": 98.5,
                  "Pooja": 99.8,
                  "Rohan": 86.2,
                  "Kartik": 79}

def get_marks(student):
    if student in students_marks:
        print(f"{student}'s marks: {students_marks[student]}")
    else:
        print(f"Student not found.")

student_name = input("Enter the student's name: ").strip().capitalize()
get_marks(student_name)
