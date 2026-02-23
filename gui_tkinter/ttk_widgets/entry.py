import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x200")

entry = ttk.Entry(root)
entry.pack()

def on_submit():
    print(entry.get())
button = tk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()