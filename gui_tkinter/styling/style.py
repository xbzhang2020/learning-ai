from tkinter import ttk
import tkinter as tk

root = tk.Tk()
root.title("Style Example")
root.geometry("800x600")


style = ttk.Style()
style.configure("My.TLabel", foreground="red", background="blue")
label = ttk.Label(root, text="Hello, World!", style="My.TLabel")


label.pack()

root.mainloop()
