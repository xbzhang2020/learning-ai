import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Checkbox Example")
root.geometry("300x200")

var = tk.BooleanVar()
checkbox = ttk.Checkbutton(root, text="Check this box", variable=var)
checkbox.pack()

def get_value():
    print(var.get())

btn = tk.Button(root, text="Get Value", command=get_value)
btn.pack()

root.mainloop()