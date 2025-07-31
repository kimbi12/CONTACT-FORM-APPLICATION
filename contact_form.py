# import csv
# import os
# with open('contacts.csv', mode='w', newline='') as file:
    # writer = csv.writer(file)
    # writer.writerow(["Name", "Email", "Phone", "Address"])
   
import tkinter as tk
from tkinter import messagebox
import csv

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()

    if not (name and email and phone and address):
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, address])
    
    messagebox.showinfo("Success", "Contact saved successfully!")
    clear_form()

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Form")
root.geometry("300x300")

# Labels and Entries
tk.Label(root, text="Full Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Phone").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5, sticky="e")

name_entry = tk.Entry(root, width=30)
email_entry = tk.Entry(root, width=30)
phone_entry = tk.Entry(root, width=30)
address_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1, pady=5)
email_entry.grid(row=1, column=1, pady=5)
phone_entry.grid(row=2, column=1, pady=5)
address_entry.grid(row=3, column=1, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
