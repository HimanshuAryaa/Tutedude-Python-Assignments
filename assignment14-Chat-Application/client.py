import socket
import threading
from tkinter import *
from tkinter import messagebox


# Function to Send & Receive Message
def send():
    message = entry.get()
    try:
        listbox.insert(END, "Client:" + message)
        entry.delete(0, END)
        s.send(message.encode("utf-8"))

        if message.lower() == "bye":
            close_connection()
    except:
        messagebox.showerror("Error", "Failed to send message")

def receive():
    while True:
        try:
            message = s.recv(50).decode("utf-8")
            if message == "bye":
                listbox.insert('end', "Server Disconnected")
                close_connection()
                break
            listbox.insert('end', "Server:" + message)
        except:
            break

def close_connection():
    try:
        s.close()
        root.destroy()
    except:
        root.destroy()


# Gui Design
root = Tk()
root.title("Chat Application - Client Side")
root.geometry("400x500")

list_frame = Frame(root)
list_frame.pack(fill='both', expand=True, padx=10, pady=10)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')
listbox = Listbox(list_frame, yscrollcommand=scrollbar.set, font=("Arial", 10))
listbox.pack(side='left', fill='both', expand=True)
scrollbar.config(command=listbox.yview)
listbox.insert(END, "------ YOUR CHAT HISTORY ------")
listbox.itemconfig(0, {'fg': 'blue'})
entry = Entry(root, font= ("Arial", 11))
entry.pack(fill='x', padx=10, pady=5)
button_frame = Frame(root)
button_frame.pack(side='bottom', fill='x', pady=10)
snd_button = Button(button_frame, text="Send", bg="#4CAF50", fg="white", width=12, command=lambda: send())
snd_button.pack(side='left', padx=20, expand=True)

# Socket Connection
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    port = 12345
    s.connect((host_name, port))

    listbox.insert("end", "Connected To server!")

    thread = threading.Thread(target=receive)
    thread.daemon = True
    thread.start()

except Exception as e:
    messagebox.showerror("Error", f"Connection failed: {e}")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_connection)
root.mainloop()