import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.result_var = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root, height=50, bg="black")
        display_frame.pack(fill="x")
        
        display_label = tk.Label(display_frame, textvariable=self.result_var, anchor="e", bg="Black", fg="Yellow", font=("Arial", 24))
        display_label.pack(expand=True, fill="both")
        
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill="both")
        buttons = [
            ("C", 1, 0), ("±", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
        ]
        
        for (text, row, col) in buttons:
            if text == "0":
                button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
                button.grid(row=row, column=col, columnspan=2, sticky="nsew")
            else:
                button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
                button.grid(row=row, column=col, sticky="nsew")
        
        for i in range(6):
            buttons_frame.rowconfigure(i, weight=1)
            buttons_frame.columnconfigure(i % 4, weight=1)
    
    def on_button_click(self, char):
        if char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = "Error"
        elif char == "C":
            self.expression = ""
        elif char == "±":
            if self.expression:
                if self.expression[0] == "-":
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
        elif char == "%":
            try:
                self.expression = str(eval(self.expression) / 100)
            except Exception as e:
                self.expression = "Error"
        else:
            self.expression += str(char)
        
        self.result_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()