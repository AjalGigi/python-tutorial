# Q18. GUI - Calculator (Add, Subtract, Multiply, Divide)

import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2

        entry_result.config(state=tk.NORMAL)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state="readonly")

    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer values.")

root = tk.Tk()
root.title("Q18 - Calculator")
root.geometry("340x250")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

tk.Label(root, text="Simple Calculator", font=("Arial", 14, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=5)

tk.Label(frame, text="Number 1:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_num1 = tk.Entry(frame, font=("Arial", 11), width=15)
entry_num1.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Number 2:", bg="#f0f4f8", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_num2 = tk.Entry(frame, font=("Arial", 11), width=15)
entry_num2.grid(row=1, column=1, padx=10)

tk.Label(frame, text="Result:", bg="#f0f4f8", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_result = tk.Entry(frame, font=("Arial", 11), width=15, state="readonly", readonlybackground="#dfe6e9")
entry_result.grid(row=2, column=1, padx=10)

btn_frame = tk.Frame(root, bg="#f0f4f8")
btn_frame.pack(pady=10)

for i, op in enumerate(["Add", "Subtract", "Multiply", "Divide"]):
    colors = {"Add": "#2ecc71", "Subtract": "#e74c3c", "Multiply": "#3498db", "Divide": "#9b59b6"}
    tk.Button(btn_frame, text=op, width=8,
              command=lambda o=op: calculate(o),
              bg=colors[op], fg="white", font=("Arial", 10),
              relief=tk.FLAT, padx=4, pady=3).grid(row=0, column=i, padx=5)

root.mainloop()
