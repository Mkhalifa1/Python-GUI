import tkinter as tk

def disable_text():
    text['state'] = 'disabled'

def enable_text():
    text['state'] = 'normal'

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Text Widget State Example')

    text = tk.Text(root, height=10, width=40)
    text.pack(padx=10, pady=10)

    btn_disable = tk.Button(root, text='Disable Text', command=disable_text)
    btn_disable.pack(pady=5)

    btn_enable = tk.Button(root, text='Enable Text', command=enable_text)
    btn_enable.pack(pady=5)

    initial_text = "You can edit this text.\nTry typing something!"
    text.insert(tk.END, initial_text)

    root.mainloop()
