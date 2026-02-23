from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("TTK Combo Box Example")
root.geometry("300x200")

combo_var = tk.StringVar()
combo_options = ["Option 1", "Option 2", "Option 3"]
combo_box = ttk.Combobox(root, textvariable=combo_var, values=combo_options)
combo_box.pack()

def on_submit():
    print(combo_var.get())
button = ttk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()