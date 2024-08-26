import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to mark a task as completed
def mark_task_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set window size and background color
root.geometry("400x400")
root.config(bg="#f0f8ff")  # Light blue background

# Create and place the title label
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#4169e1")
title_label.pack(pady=10)

# Create and place the task entry widget
task_entry = tk.Entry(root, width=30, font=("Helvetica", 12), bd=2, relief="groove")
task_entry.pack(pady=10)

# Create and place the buttons with custom styling
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

add_task_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Helvetica", 10, "bold"), bg="#4682b4", fg="white", bd=2, relief="ridge", padx=10, pady=5)
add_task_button.grid(row=0, column=0, padx=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Helvetica", 10, "bold"), bg="#dc143c", fg="white", bd=2, relief="ridge", padx=10, pady=5)
delete_task_button.grid(row=0, column=1, padx=10)

mark_completed_button = tk.Button(button_frame, text="Mark Completed", command=mark_task_completed, font=("Helvetica", 10, "bold"), bg="#32cd32", fg="white", bd=2, relief="ridge", padx=10, pady=5)
mark_completed_button.grid(row=0, column=2, padx=10)

# Create and place the listbox to display tasks with a scrollbar
tasks_frame = tk.Frame(root, bg="#f0f8ff")
tasks_frame.pack(pady=10)

tasks_scrollbar = tk.Scrollbar(tasks_frame)
tasks_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tasks_listbox = tk.Listbox(tasks_frame, width=50, height=10, font=("Helvetica", 12), bd=2, relief="groove", yscrollcommand=tasks_scrollbar.set, selectbackground="#87ceeb")
tasks_listbox.pack()

tasks_scrollbar.config(command=tasks_listbox.yview)

# Start the Tkinter event loop
root.mainloop()
