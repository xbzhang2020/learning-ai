import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TTK Label Example")
root.geometry("300x200")

label = ttk.Label(root, text="Hello, World!")
label.pack()

root.mainloop()