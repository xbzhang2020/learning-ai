import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Table Example")
root.geometry("800x600")

data = [
    {"id": 1, "name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 2, "name": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "name": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 4, "name": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"id": 5, "name": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
]
columns = ["name", "author", "year"]

tv = ttk.Treeview(root, columns=columns, selectmode="none")

# 添加表头
tv.heading("#0", text="ID")
for col in columns:
    tv.heading(col, text=col.capitalize())

colors = ["red", "green", "blue", "yellow", "purple"]

# 添加数据
for i, item in enumerate(data):
    tag = f"tag_{i}"
    tv.tag_configure(tag, background=colors[i])
    values = [item[key] for key in columns]
    tv.insert('', "end", text=item["id"], values=values, tags=[tag])

tv.pack()

root.mainloop()
