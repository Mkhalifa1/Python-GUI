import tkinter as tk

def display_text():
    text_content = text.get('1.0', 'end')
    print(text_content)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Get Text Example')

    text = tk.Text(root, height=5, width=30)
    text.pack(padx=10, pady=10)

    btn_display = tk.Button(root, text='Display Text', command=display_text)
    btn_display.pack(pady=5)

    root.mainloop()
