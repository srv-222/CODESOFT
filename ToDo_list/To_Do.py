import tkinter as tk
from tkinter import messagebox

tasks = {}
task_counter = 0

def add_task():
    global task_counter
    new_task = task_input.get()
    if new_task.strip():
        task_counter += 1
        tasks[task_counter] = new_task
        messagebox.showinfo("Task Added", "Task successfully recorded!")
        print(f"Added task {task_counter}: {new_task}")
        task_input.delete(0, tk.END)
    else:
        messagebox.showinfo("Invalid Entry", "Please enter a task before adding.")
        task_input.delete(0, tk.END)

def show_tasks():
    task_box.delete(0, tk.END)
    if tasks:
        for num, text in tasks.items():
            task_box.insert(tk.END, f"{num}) {text}")
    else:
        messagebox.showinfo("No Tasks Found", "There are no tasks in your list.")
        print("No items to display.")

def remove_all():
    global tasks, task_counter
    if tasks:
        tasks.clear()
        task_counter = 0
        task_box.delete(0, tk.END)
        messagebox.showinfo("Cleared", "All tasks have been removed.")
    else:
        messagebox.showinfo("Empty List", "Nothing to delete here.")

def remove_task():
    global tasks, task_counter
    try:
        remove_index = int(delete_input.get())
        if remove_index in tasks:
            del tasks[remove_index]
            messagebox.showinfo("Deleted", f"Task #{remove_index} has been removed.")
            print(f"Removed task #{remove_index}")
            # Re-indexing remaining tasks
            tasks = {i+1: v for i, v in enumerate(tasks.values())}
            task_counter = len(tasks)
            delete_input.delete(0, tk.END)
            show_tasks()
        else:
            messagebox.showinfo("Not Found", "That task number does not exist.")
            delete_input.delete(0, tk.END)
    except Exception as ex:
        print("Invalid input for deletion:", ex)
        messagebox.showinfo("Error", "Please enter a valid number.")

def quit_app():
    messagebox.showinfo("Goodbye", "Thanks for using the To-Do app!")
    print("App closed.")
    root.destroy()

# ========== GUI ========== #

root = tk.Tk()
root.title("Task Manager")
root.geometry("700x700")
root.configure(bg="white")

# Title
tk.Label(root, text="My Task List", font=("Verdana", 24, "bold"), fg="navy", bg="white").pack(pady=20)

# Input section
input_frame = tk.Frame(root, bg="white")
input_frame.pack(pady=10)

tk.Label(input_frame, text="What do you need to do?", font=("Calibri", 14), bg="white").grid(row=0, column=0, padx=5)
task_input = tk.Entry(input_frame, font=("Calibri", 14), width=30)
task_input.grid(row=0, column=1, padx=5)
tk.Button(input_frame, text="Add", font=("Calibri", 14), bg="green", fg="white", command=add_task).grid(row=0, column=2, padx=5)

# Task display
display_frame = tk.Frame(root, bg="white")
display_frame.pack(pady=10)

tk.Label(display_frame, text="Your tasks so far:", font=("Calibri", 16, "bold"), bg="white").pack()
task_box = tk.Listbox(display_frame, width=50, height=10, font=("Segoe UI", 12))
task_box.pack(pady=5)

# View/Delete All Buttons
action_frame = tk.Frame(root, bg="white")
action_frame.pack(pady=10)

tk.Button(action_frame, text="Show All", font=("Calibri", 12), bg="blue", fg="white", command=show_tasks).grid(row=0, column=0, padx=10)
tk.Button(action_frame, text="Clear All", font=("Calibri", 12), bg="red", fg="white", command=remove_all).grid(row=0, column=1, padx=10)

# Delete single task
delete_frame = tk.Frame(root, bg="white")
delete_frame.pack(pady=10)

tk.Label(delete_frame, text="Task number to delete:", font=("Calibri", 14), bg="white").grid(row=0, column=0, padx=5)
delete_input = tk.Entry(delete_frame, font=("Calibri", 14), width=10)
delete_input.grid(row=0, column=1, padx=5)
tk.Button(delete_frame, text="Delete", font=("Calibri", 12), bg="red", fg="white", command=remove_task).grid(row=0, column=2, padx=5)

# Exit
tk.Button(root, text="Close App", font=("Calibri", 12), bg="black", fg="white", command=quit_app).pack(pady=20)

root.mainloop()
