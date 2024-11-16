import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("To-Do List Application")

tasks = []

def update_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update a selected task
def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index] = task_entry.get()
        update_list()
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        update_list()
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task.")

# Create the GUI components
task_frame = tk.Frame(win)
task_frame.pack()

task_listbox = tk.Listbox(task_frame, width=50, height=10)
task_listbox.pack(side=tk.LEFT)

task_entry = tk.Entry(win, width=52)
task_entry.pack()

add = tk.Button(win, text="Add Task", command=add_task,bg='beige',fg='black')
add.pack()

update = tk.Button(win, text="Update Task", command=update_task,bg='beige',fg='black')
update.pack()

delete = tk.Button(win, text="Delete Task", command=delete_task,bg='beige',fg='black')
delete.pack()

win.configure(bg='lightpink')

win.mainloop()
