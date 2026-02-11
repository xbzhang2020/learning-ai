import tkinter as tk

root = tk.Tk()
root.title("Banana interest Survey")
root.geometry("800x600")
root.resizable(False, False)

label = tk.Label(root, text="Please take the survery")
label.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name = tk.Entry(root)
name.pack()

eater = tk.Checkbutton(root, text="Check this box if you eat bananas")
eater.pack()

num_label = tk.Label(root, text="Number of bananas eaten per day:")
num_label.pack()
num = tk.Spinbox(root, from_=0, to=100)
num.pack()

plantain_label = tk.Label(root, text="Do you like plantains?")
plantain_frame = tk.Frame(root)
plantain_yes = tk.Radiobutton(plantain_frame, text="Yes")
plantain_no = tk.Radiobutton(plantain_frame, text="No")
plantain_yes.pack()
plantain_no.pack()
plantain_label.pack()
plantain_frame.pack()

banana_haiku_label = tk.Label(root, text="Write a haiku about bananas:")
banana_haiku_label.pack()
banana_haiku = tk.Text(root, height=3)
banana_haiku.pack()

def on_submit():
    print('Hello, World!')

submit = tk.Button(root, text="Submit", command=on_submit)
submit.pack()

root.mainloop()
