import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Advanced Python Calculator")
root.geometry("400x600")
root.resizable(False, False)

expression = ""

# Input/output display
entry = tk.Entry(root, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=5, pady=20, padx=10)
entry.focus()

# History list
history = []

def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def backspace():
    global expression
    expression = expression[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        history.append(expression + " = " + result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()

def show_history():
    if history:
        messagebox.showinfo("Calculation History", "\n".join(history[-5:]))
    else:
        messagebox.showinfo("Calculation History", "No history yet.")

def apply_function(func):
    global expression
    try:
        result = str(func(float(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = result
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('log', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('sin', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('cos', 4, 4),
    ('(', 5, 0), (')', 5, 1), ('π', 5, 2), ('e', 5, 3), ('tan', 5, 4),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        cmd = equal
    elif text == 'π':
        cmd = lambda x=pi: press(x)
    elif text == 'e':
        cmd = lambda x=e: press(x)
    elif text == 'sin':
        cmd = lambda f=sin: apply_function(f)
    elif text == 'cos':
        cmd = lambda f=cos: apply_function(f)
    elif text == 'tan':
        cmd = lambda f=tan: apply_function(f)
    elif text == 'log':
        cmd = lambda f=log: apply_function(f)
    elif text == 'sqrt':
        cmd = lambda f=sqrt: apply_function(f)
    else:
        cmd = lambda x=text: press(x)

    tk.Button(root, text=text, width=6, height=2, font=('Arial', 14),
              command=cmd).grid(row=row, column=col, padx=3, pady=3)

# Extra utility buttons
tk.Button(root, text='C', width=13, height=2, font=('Arial', 14), command=clear).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text='⌫', width=6, height=2, font=('Arial', 14), command=backspace).grid(row=6, column=2, padx=5, pady=5)
tk.Button(root, text='HIST', width=13, height=2, font=('Arial', 14), command=show_history).grid(row=6, column=3, columnspan=2, padx=5, pady=5)

# Enable keyboard input
def keypress(event):
    char = event.char
    if char in '0123456789.+-*/()':
        press(char)
    elif event.keysym == 'Return':
        equal()
    elif event.keysym == 'BackSpace':
        backspace()
    elif event.keysym == 'Escape':
        clear()

root.bind('<Key>', keypress)

# Run the application
root.mainloop()
