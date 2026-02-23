import tkinter as tk

root = tk.Tk()
root.title("Button Example")
root.geometry("300x200")

button = tk.Button(root, text="Click me")
button.pack()

root.mainloop()