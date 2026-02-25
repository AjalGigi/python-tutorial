# Q20. GUI - Bill Generator with Discount

import tkinter as tk
from tkinter import messagebox

def generate_bill():
    try:
        price = float(entry_price.get())
        quantity = int(entry_qty.get())

        if price < 0 or quantity < 0:
            raise ValueError("Values must be positive.")

        total = price * quantity
        discount = 0.0

        if total > 1000:
            discount = total * 0.10  # 10% discount

        final_amount = total - discount

        entry_result.config(state=tk.NORMAL)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"₹{final_amount:.2f}  (Discount: ₹{discount:.2f})")
        entry_result.config(state="readonly")

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter valid numeric values.\n{e}")

root = tk.Tk()
root.title("Q20 - Bill Generator")
root.geometry("380x230")
root.resizable(False, False)
root.configure(bg="#f0f4f8")

tk.Label(root, text="Bill Generator", font=("Arial", 14, "bold"),
         bg="#f0f4f8", fg="#2c3e50").pack(pady=10)

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=5)

tk.Label(frame, text="Item Price (₹):", bg="#f0f4f8", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_price = tk.Entry(frame, font=("Arial", 11), width=18)
entry_price.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Quantity:", bg="#f0f4f8", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_qty = tk.Entry(frame, font=("Arial", 11), width=18)
entry_qty.grid(row=1, column=1, padx=10)

tk.Label(frame, text="Final Amount:", bg="#f0f4f8", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_result = tk.Entry(frame, font=("Arial", 11), width=25, state="readonly", readonlybackground="#dfe6e9")
entry_result.grid(row=2, column=1, padx=10)

tk.Button(root, text="Generate Bill", command=generate_bill,
          bg="#9b59b6", fg="white", font=("Arial", 12, "bold"),
          relief=tk.FLAT, padx=10, pady=5).pack(pady=12)

root.mainloop()
