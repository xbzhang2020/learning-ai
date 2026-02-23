import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

# messagebox.showinfo(title="Info", message="This is an info message")
# messagebox.showerror(title="Error", message="This is an error message")
# messagebox.showwarning(title="Warning", message="This is a warning message")

# quit = messagebox.askyesno(title="Confirm", message="Are you sure you want to quit?")

# if quit:
#     print("You chose to quit")
#     exit()
# else:
#     print("You chose to stay")

# file = filedialog.askopenfile(title="Open", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
# if file:
#     print(file.name)
# else:
#     print("No file selected")

# filename = filedialog.asksaveasfilename(title="Save", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
# if filename:
#     print(filename)
# else:
#     print("No file selected")

# name = simpledialog.askstring(title="Input", prompt="What is your name?")
# if name:
#     print(name)
# else:
#     print("No name entered")

class LoginDialog(simpledialog.Dialog):
    def __init__(self, parent):
        super().__init__(parent)

    def body(self, master):
        self.title("Login")
        self.geometry("300x200")
        self.resizable(False, False)

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master)
        self.password_entry.pack()

    def buttonbox(self):
        box = tk.Frame(self)
        w = tk.Button(box, text="OK", width=5, command=self.ok)
        w.pack(side=tk.LEFT, padx=5)
        w = tk.Button(box, text="Cancel", width=5, command=self.cancel)
        w.pack(side=tk.LEFT, padx=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def login(self):
        print(self.username_entry.get(), self.password_entry.get())

if __name__ == "__main__":
    root = tk.Tk()
    LoginDialog(root)
    root.mainloop()