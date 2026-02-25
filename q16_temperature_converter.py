# Q16. GUI - Temperature Converter (Celsius to Fahrenheit)

import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9 / 5) + 32
        entry_result.config(state=tk.NORMAL)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{fahrenheit:.2f}")
        entry_result.config(state="readonly")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")

root = tk.Tk()
root.title("Q16 - Temperature Converter")
root.geometry("340x200")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

tk.Label(root, text="Temperature Converter", font=("Arial", 14, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=5)

tk.Label(frame, text="Celsius:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_celsius = tk.Entry(frame, font=("Arial", 11), width=15)
entry_celsius.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Fahrenheit:", bg="#f0f4f8", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_result = tk.Entry(frame, font=("Arial", 11), width=15, state="readonly", readonlybackground="#dfe6e9")
entry_result.grid(row=1, column=1, padx=10)

tk.Button(root, text="Convert to Fahrenheit", command=convert,
          bg="#3498db", fg="white", font=("Arial", 11),
          relief=tk.FLAT, padx=8, pady=4).pack(pady=10)

root.mainloop()
