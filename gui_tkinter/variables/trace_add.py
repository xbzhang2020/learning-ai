import tkinter as tk

root = tk.Tk()
root.title("Trace Add Example")
root.geometry("300x200")

num_var = tk.IntVar()
spinbox = tk.Spinbox(root, from_=0, to=100, textvariable=num_var)

def on_change(*args, **kwargs):
    label_var.set(f"Value: {num_var.get()}")

label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var)
num_var.trace_add("write", on_change)


spinbox.pack()
label.pack()

root.mainloop()
