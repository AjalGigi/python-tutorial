# Q15. GUI with Label, Clear and Restore Buttons

import tkinter as tk

def clear_label():
    label.config(text="")
    btn_clear.config(state=tk.DISABLED)
    btn_restore.config(state=tk.NORMAL)

def restore_label():
    label.config(text="Python GUI Demo")
    btn_restore.config(state=tk.DISABLED)
    btn_clear.config(state=tk.NORMAL)

# Main window
root = tk.Tk()
root.title("Q15 - GUI Demo")
root.geometry("320x160")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

label = tk.Label(root, text="Python GUI Demo", font=("Arial", 16, "bold"),
                 bg="#f0f4f8", fg="#2c3e50")
label.pack(pady=30)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

btn_clear = tk.Button(frame, text="Clear", width=10, command=clear_label,
                      bg="#e74c3c", fg="white", font=("Arial", 11),
                      relief=tk.FLAT, padx=5, pady=3)
btn_clear.grid(row=0, column=0, padx=10)

btn_restore = tk.Button(frame, text="Restore", width=10, command=restore_label,
                        bg="#2ecc71", fg="white", font=("Arial", 11),
                        relief=tk.FLAT, padx=5, pady=3, state=tk.DISABLED)
btn_restore.grid(row=0, column=1, padx=10)

root.mainloop()
