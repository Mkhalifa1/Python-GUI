import tkinter as tk

def create_text_widget():
    root = tk.Tk()
    root.title('Text Widget Example')

    # Define the default configuration using a dictionary (cnf)
    text_config = {
        'width': 40,
        'height': 10,
        'wrap': tk.WORD  # Wrap text at word boundaries
    }

    # Create the Text widget with the default configuration (cnf) and additional keyword arguments (kw)
    text_widget = tk.Text(root, **text_config, font=('Arial', 12), fg='blue', bg='lightyellow')

    # Insert some initial text
    initial_text = "This is a Text widget.\nYou can type and edit multiple lines of text here."
    text_widget.insert(tk.END, initial_text)

    text_widget.pack(padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    create_text_widget()
