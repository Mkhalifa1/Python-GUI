import tkinter as tk


# Create the main tkinter window
root = tk.Tk()
root.geometry("300x200")  # Set the window size (width x height)

# Create the button
button = tk.Button(root, text="Centered Button")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the tkinter main loop
root.mainloop()
