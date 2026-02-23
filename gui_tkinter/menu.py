import tkinter as tk

root = tk.Tk()
root.title("Menu Example")
root.geometry("300x200")

menu = tk.Menu(root)
root.config(menu=menu)

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add("command", label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))


root.mainloop()