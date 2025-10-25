import tkinter as tk
from calculator import add, subtract, multiply, divide

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if operation == '+':
            result.set(add(a, b))
        elif operation == '-':
            result.set(subtract(a, b))
        elif operation == '*':
            result.set(multiply(a, b))
        elif operation == '/':
            result.set(divide(a, b))
    except Exception as e:
        result.set(f"Error: {e}")

# ----->Window setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("250x250")

# ----->Inputs
tk.Label(root, text="A:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="B:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# ----->Result
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack(pady=10)

# ----->Buttons
tk.Button(root, text="+", command=lambda: calculate('+')).pack(fill='x')
tk.Button(root, text="-", command=lambda: calculate('-')).pack(fill='x')
tk.Button(root, text="*", command=lambda: calculate('*')).pack(fill='x')
tk.Button(root, text="/", command=lambda: calculate('/')).pack(fill='x')

root.mainloop()