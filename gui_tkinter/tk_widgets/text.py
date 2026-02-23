import tkinter as tk

root = tk.Tk()
root.title("Text Example")
root.geometry("300x200")

my_text = tk.Text(root, height=3)
my_text.insert(tk.END, "<h1>Hello, World!</h1>")
my_text.pack()

def on_submit():
    print(my_text.get('1.0', tk.END))
button = tk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()