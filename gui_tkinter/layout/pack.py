import tkinter as tk

root = tk.Tk()
root.title("Pack Layout Example")
root.geometry("300x200")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Name:")
label.pack(side=tk.LEFT)

name = tk.Entry(frame)
name.pack(side=tk.LEFT)

root.mainloop()