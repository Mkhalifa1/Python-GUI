import tkinter as tk


root = tk.Tk()
root.title('Tkinter Window Demo')
root.geometry('300x200+50+50')
root.resizable(0, 0)
root.attributes('-topmost', 1)

root.mainloop()
