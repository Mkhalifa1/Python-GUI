import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Login')
root.geometry("350x220")


fields = {}

fields['username_label'] = ttk.Label(text='Username:')
fields['username'] = ttk.Entry()

fields['password_label'] = ttk.Label(text='Password:')
fields['password'] = ttk.Entry(show="*")


for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=5)

root.mainloop()
