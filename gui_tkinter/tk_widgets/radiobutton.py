import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("300x200")

var = tk.StringVar()
radio_button1 = tk.Radiobutton(root, text="Yes", value=True, variable=var)
radio_button2 = tk.Radiobutton(root, text="No", value=False, variable=var)

radio_button1.grid(row=0, column=0)
radio_button2.grid(row=0, column=1)

def on_submit():
    print(var.get())
button = tk.Button(root, text="Submit", command=on_submit)
button.grid(row=1, column=0, columnspan=2)

root.mainloop()