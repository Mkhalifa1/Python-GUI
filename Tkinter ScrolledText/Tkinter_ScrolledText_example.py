import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

# Create a ScrolledText widget
scrolled_text = scrolledtext.ScrolledText(root, width=40, height=10)

# Add some text to the ScrolledText widget
scrolled_text.insert(tk.END, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 20)

# Pack the ScrolledText widget
scrolled_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()




