import tkinter as tk


class BoundText(tk.Text):
    """
    A Text widget that is bound to a StringVar.
    """

    def __init__(self, parent, textvariable, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._var = textvariable
        if self._var:
            self.insert("1.0", self._var.get())
            self._var.trace_add("write", self._set_content)
            self.bind("<<Modified>>", self._set_var)

    def _set_content(self, *_):
        self.delete("1.0", tk.END)
        self.insert("1.0", self._var.get())

    def _set_var(self, *_):
        if self.edit_modified():
            content = self.get("1.0", "end-1chars")
            self._var.set(content)
            self.edit_modified(False)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bound Text Example")
    root.geometry("300x200")

    text_var = tk.StringVar()
    text = BoundText(root, text_var)
    text.pack()

    submit_button = tk.Button(
        root, text="Submit", command=lambda: print(text_var.get())
    )
    submit_button.pack()

    root.mainloop()
