import tkinter as tk
import json


class JSONVar(tk.StringVar):
    """
    A variable that stores JSON data.
    """

    def __init__(self, *args, **kwargs):
        kwargs["value"] = json.dumps(kwargs.get("value", {}))
        super().__init__(*args, **kwargs)

    def set(self, value, *args, **kwargs):
        new_value = json.dumps(value)
        super().set(new_value, *args, **kwargs)

    def get(self, *args, **kwargs):
        value = super().get(*args, **kwargs)
        return json.loads(value)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("JSONVar Example")
    root.geometry("300x200")

    json_var = JSONVar()
    json_var.set({"name": "John", "age": 30})
    print(json_var.get())

    root.mainloop()
