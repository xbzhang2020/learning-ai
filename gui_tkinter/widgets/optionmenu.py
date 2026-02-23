import tkinter as tk

root = tk.Tk()
root.title("Option Menu Example")
root.geometry("300x200")

option_var = tk.StringVar()
options = ["Option 1", "Option 2", "Option 3"]
option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.pack()

def on_submit():
    print(option_var.get())
button = tk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()