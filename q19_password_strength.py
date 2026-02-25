# Q19. GUI - Password Strength Checker

import tkinter as tk
import re

def check_strength():
    password = entry_password.get()

    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    length = len(password)

    if length >= 8 and has_digit and has_special:
        strength = "Strong 💪"
        color = "#27ae60"
    elif length >= 6 and (has_digit or has_special):
        strength = "Moderate 🔶"
        color = "#f39c12"
    else:
        strength = "Weak ❌"
        color = "#e74c3c"

    label_result.config(text=strength, fg=color)

root = tk.Tk()
root.title("Q19 - Password Strength Checker")
root.geometry("340x200")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

tk.Label(root, text="Password Strength Checker", font=("Arial", 13, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=15)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

tk.Label(frame, text="Password:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=10, sticky="e")
entry_password = tk.Entry(frame, font=("Arial", 11), width=20, show="*")
entry_password.grid(row=0, column=1, padx=10)

tk.Button(root, text="Check Strength", command=check_strength,
          bg="#3498db", fg="white", font=("Arial", 11),
          relief=tk.FLAT, padx=8, pady=4).pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 13, "bold"), bg="#f0f4f8")
label_result.pack()

root.mainloop()
