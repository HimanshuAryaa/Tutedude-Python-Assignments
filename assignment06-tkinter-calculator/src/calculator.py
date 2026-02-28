from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("310x300")

# Global
result = 0
math = ""

# Input
display_box = Entry(window, width=50, borderwidth=5, justify="right")
display_box.place(x=00, y=0)
display_box.insert(0, '0')
display_box.bind('<Key>', lambda event: 'break')

# Functions
def button_clicked(number):
    current = display_box.get()
    if "Can't" in current:
        display_box.delete(0, END)
    if current == '0':
        display_box.delete(0, END)
        display_box.insert(0, str(number))
    else:
        display_box.insert(END, str(number))

def operations(operation):
    if "Can't" in display_box.get():
        display_box.delete(0, END)
        display_box.insert(0, '0')
        return
    first_number = display_box.get()
    global result, math
    result = int(first_number)
    math = operation
    display_box.delete(0, END)

def clear():
    display_box.delete(0, END)
    display_box.insert(0, '0')

def equal():
    global result
    if "Can't" in display_box.get():
        display_box.delete(0, END)
        display_box.insert(0, '0')
        return
    second_number = display_box.get()
    display_box.delete(0, END)
    try:
        if math == 'add':
            result = result + int(second_number)
            display_box.insert(0, str(result))
        elif math == 'sub':
            result = result - int(second_number)
            display_box.insert(0, str(result))
        elif math == 'mul':
            result = result * int(second_number)
            display_box.insert(0, str(result))
        elif math == 'div':
            result = result / int(second_number)
            display_box.insert(0, str(result))
    except ZeroDivisionError:
        display_box.insert(0, "Can't divide by zero")

#Buttons
button_1 = Button(window, text='1', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(1))
button_2 = Button(window, text='2', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(2))
button_3 = Button(window, text='3', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(3))
button_4 = Button(window, text='4', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(4))
button_5 = Button(window, text='5', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(5))
button_6 = Button(window, text='6', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(6))
button_7 = Button(window, text='7', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(7))
button_8 = Button(window, text='8', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(8))
button_9 = Button(window, text='9', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(9))
button_add = Button(window, text='+', width=12, fg='White', bg='#3E3A38', command=lambda: operations("add"))
button_0 = Button(window, text='0', width=12, fg='White', bg='#3E3A38', command=lambda: button_clicked(0))
button_sub = Button(window, text='-', width=12, fg='White', bg='#3E3A38', command=lambda: operations("sub"))
button_mul = Button(window, text='*', width=12, fg='White', bg='#3E3A38', command=lambda: operations("mul"))
button_div = Button(window, text='/', width=12, fg='White', bg='#3E3A38', command=lambda: operations("div"))
button_clear = Button(window, text='⌫', width=12, fg='White', bg='#3E3A38', command=clear)
button_equal = Button(window, text='=', width=39, fg='White', bg='#35312F', command=equal)

#Buttons - Positions
button_1.place(x=10, y=60)
button_2.place(x=105, y=60)
button_3.place(x=200, y=60)
button_4.place(x=10, y=90)
button_5.place(x=105, y=90)
button_6.place(x=200, y=90)
button_7.place(x=10, y=120)
button_8.place(x=105, y=120)
button_9.place(x=200, y=120)
button_add.place(x=10, y=150)
button_0.place(x=105, y=150)
button_sub.place(x=200, y=150)
button_mul.place(x=10, y=180)
button_div.place(x=105, y=180)
button_clear.place(x=200, y=180)
button_equal.place(x=10, y=210)

# Mainloop
window.mainloop()
