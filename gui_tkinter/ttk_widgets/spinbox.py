import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Spinbox Example")
root.geometry("300x200")

num_var = tk.IntVar()
spinbox = ttk.Spinbox(root, from_=0, to=100, textvariable=num_var)
spinbox.pack()

def on_submit():
    print(num_var.get())
button = ttk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()