import tkinter as tk
from tkinter import ttk


class LabelInput(tk.Frame):
    """
    A frame that contains a label and an input field.
    """

    def __init__(
        self, parent, label, inp_cls=ttk.Entry, inp_kwargs=None, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        self.label = ttk.Label(self, text=label, anchor=tk.W)
        self.label.pack(side=tk.LEFT)
        self.input = inp_cls(self, **(inp_kwargs or {}))
        self.input.pack(side=tk.RIGHT)


class MyForm(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._vars = {"name": tk.StringVar(), "password": tk.StringVar()}

        self.name = LabelInput(
            self, "Name", tk.Entry, inp_kwargs={"textvariable": self._vars["name"]}
        )
        self.password = LabelInput(
            self,
            "Password",
            tk.Entry,
            inp_kwargs={"textvariable": self._vars["password"]},
        )
        self.submit = tk.Button(self, text="Submit", command=self._on_submit)

        self.name.grid(row=0, column=0)
        self.password.grid(row=1, column=0)
        self.submit.grid(row=2, column=0)

    def _on_submit(self):
        data = {key: self._vars[key].get() for key in self._vars.keys()}
        print(data)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My Form Example")
        self.geometry("300x200")


if __name__ == "__main__":
    root = Application()

    my_form = MyForm(root)
    my_form.pack()

    root.mainloop()
