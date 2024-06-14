import random
import string
import tkinter as tk
from tkinter import ttk

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.password_length = tk.IntVar(value=12)
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(expand=True, fill="both")

        length_label = ttk.Label(frame, text="Password Length:")
        length_label.grid(row=0, column=0, sticky="w")

        length_spinbox = ttk.Spinbox(frame, from_=6, to=32, textvariable=self.password_length, width=5)
        length_spinbox.grid(row=0, column=1, sticky="w")

        uppercase_check = ttk.Checkbutton(frame, text="Include Uppercase Letters", variable=self.include_uppercase)
        uppercase_check.grid(row=1, column=0, columnspan=2, sticky="w")

        lowercase_check = ttk.Checkbutton(frame, text="Include Lowercase Letters", variable=self.include_lowercase)
        lowercase_check.grid(row=2, column=0, columnspan=2, sticky="w")

        digits_check = ttk.Checkbutton(frame, text="Include Digits", variable=self.include_digits)
        digits_check.grid(row=3, column=0, columnspan=2, sticky="w")

        special_check = ttk.Checkbutton(frame, text="Include Special Characters", variable=self.include_special)
        special_check.grid(row=4, column=0, columnspan=2, sticky="w")

        generate_button = ttk.Button(frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(frame, textvariable=self.password_var, state="readonly", width=50)
        password_entry.grid(row=6, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.password_length.get()
        characters = ""

        if self.include_uppercase.get():
            characters += string.ascii_uppercase
        if self.include_lowercase.get():
            characters += string.ascii_lowercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            self.password_var.set("Please select at least one character set")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
