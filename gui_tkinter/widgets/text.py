import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x200")

entry = tk.Text(root, height=3)
entry.insert(tk.END, "<h1>Hello, World!</h1>")
entry.pack()


def on_submit():
    print(entry.get('1.0', tk.END))
button = tk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()