import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Label Frame Example")
root.geometry("300x200")

label_frame = ttk.LabelFrame(root, text="Label Frame")
label_frame.pack()

b1 = ttk.Button(label_frame, text="Button 1")
b2 = ttk.Button(label_frame, text="Button 2")
b1.pack()
b2.pack()

root.mainloop()