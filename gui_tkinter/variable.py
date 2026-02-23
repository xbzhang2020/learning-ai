import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x200")

name_var = tk.StringVar()

name_entry = tk.Entry(root, textvariable=name_var)
name_entry.pack()

label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var)
label.pack()

def on_submit():
    label_var.set(f"Hello, {name_var.get()}!")
button = tk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()