import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TTK Button Example")
root.geometry("300x200")

button = ttk.Button(root, text="Click me")
button.pack()

root.mainloop()