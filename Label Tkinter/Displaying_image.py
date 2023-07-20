import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


# create the root window
root = tk.Tk()
root.geometry('1000x1000')
root.title('Label Widget Image')

# display an image label
photo = ImageTk.PhotoImage(Image.open("C:/Users/ENG-Mahmoud/Desktop/logo.png"))
image_label = ttk.Label(
    root,
    image=photo
)
image_label.pack()

root.mainloop()
