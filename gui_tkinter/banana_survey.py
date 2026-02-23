import tkinter as tk

root = tk.Tk()

root.title("Banana interest Survey")
root.geometry("640x480+300+300")
root.resizable(False, False)

title = tk.Label(
    root, text="Please take the survey", font=("Arial 16 bold"), bg="brown", fg="#FF0"
)

name_label = tk.Label(root, text="What is your name?")
name_var = tk.StringVar()
name = tk.Entry(root, textvariable=name_var)

eater_var = tk.BooleanVar()
eater = tk.Checkbutton(
    root, text="Check this box if you eat bananas", variable=eater_var
)

num_label = tk.Label(root, text="How many bananas do you eat per day?")
num_var = tk.IntVar()
num = tk.Spinbox(root, from_=0, to=100, textvariable=num_var)

plantain_label = tk.Label(root, text="Do you like plantains?")

plantain_frame = tk.Frame(root)
plantain_var = tk.BooleanVar()
plantain_yes = tk.Radiobutton(
    plantain_frame, text="Yes", value=True, variable=plantain_var
)
plantain_no = tk.Radiobutton(
    plantain_frame, text="No", value=False, variable=plantain_var
)


banana_haiku_label = tk.Label(root, text="Write a haiku about bananas:")
banana_haiku = tk.Text(root, height=3)


def on_submit():
    print("Hello, World!")

submit = tk.Button(root, text="Submit", command=on_submit)

output_var = tk.StringVar(value='')
output_line = tk.Label(
  root,
  textvariable=output_var,
  anchor='w',
  justify='left'
)

title.pack()
name_label.pack()
name.pack()
eater.pack()
num_label.pack()
num.pack()
plantain_yes.pack()
plantain_no.pack()
plantain_label.pack()
plantain_frame.pack()
banana_haiku_label.pack()
banana_haiku.pack()
submit.pack()

root.mainloop()
