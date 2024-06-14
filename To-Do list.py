import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=10)

        edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        edit_button.grid(row=0, column=2, padx=5, pady=10)

        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=0, column=3, padx=5, pady=10)

        clear_button = tk.Button(self.root, text="Clear All", command=self.clear_all)
        clear_button.grid(row=0, column=4, padx=5, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=5, padx=10, pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            new_task = simpledialog.askstring("Edit Task", "Enter new task:", initialvalue=selected_task)
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to edit!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.task_listbox.delete(selected_index)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def clear_all(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks = []
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
