import tkinter as tk
from tkinter import ttk

data = {
    "Project A": ["file_a.py", "file_a.txt", "something.xls"],
    "Project B": ["file_b.csv", "photo.jpg"],
    "Project C": [],
}
columns = ["file"]

root = tk.Tk()
root.title("Tree View Example")
root.geometry("800x600")

tv = ttk.Treeview(root, columns=columns)

# 添加表头
tv.heading("#0", text="Project")
for col in columns:
    tv.heading(col, text=col.capitalize())

# 添加数据
for project, files in data.items():
    tv.insert("", "end", text=project, values=files)


tv.pack()

root.mainloop()
