import tkinter
from tkinter import Label, Button, Entry


class MyWindow(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("My Application")
        self.minsize(600, 400)
        self.config(padx=30, pady=50)


if __name__ == '__main__':
    root: MyWindow = MyWindow()

    # Label
    label: tkinter.Label = tkinter.Label(root, text="Click the button below!", font=("Arial", 40, "bold"))
    label.grid(row=0, column=1)

    # Button
    button: Button = Button(text="Click Me!", font=("Ubuntu", 50, "bold"),
                            command=lambda: label.config(text=entry.get()))
    button.grid(row=0, column=0)

    # Entry
    entry: Entry = Entry(width=50, font=("Ubuntu"))
    entry.grid(row=1, column=0)


    root.mainloop(0)
