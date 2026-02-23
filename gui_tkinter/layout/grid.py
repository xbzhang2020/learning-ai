import tkinter as tk

root = tk.Tk()
root.title("Pack Layout Example")
root.geometry("300x200")

label = tk.Label(root, text="Name:")
label.grid()

name = tk.Entry(root)
name.grid(row=0, column=1)

root.mainloop()