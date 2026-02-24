import tkinter as tk

root = tk.Tk()
root.title("Message Enter Example")
root.geometry("300x200")

entry = tk.Entry(root)
entry.pack()

def on_submit(event):
    print(f"You entered: {entry.get()}")
entry.bind("<Return>", on_submit)

root.mainloop()