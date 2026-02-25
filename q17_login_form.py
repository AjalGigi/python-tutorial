# Q17. GUI - Login Form

import tkinter as tk
from tkinter import messagebox

# Hardcoded correct credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showwarning("Empty Fields", "Username and Password cannot be empty!")
        return

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login", "Login Successful! Welcome, " + username)
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password.")

root = tk.Tk()
root.title("Q17 - Login Form")
root.geometry("320x220")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

tk.Label(root, text="Login", font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=15)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

tk.Label(frame, text="Username:", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=6, sticky="e")
entry_username = tk.Entry(frame, font=("Arial", 11), width=18)
entry_username.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Password:", bg="#f0f4f8", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=6, sticky="e")
entry_password = tk.Entry(frame, font=("Arial", 11), width=18, show="*")
entry_password.grid(row=1, column=1, padx=10)

tk.Button(root, text="Login", command=login,
          bg="#2ecc71", fg="white", font=("Arial", 12, "bold"),
          relief=tk.FLAT, padx=10, pady=4).pack(pady=15)

root.mainloop()
