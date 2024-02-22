from tkinter import Canvas, Label, Tk, Button, Entry, Image
import tkinter
IMAGE_WIDTH: int = 200
IMAGE_HEIGHT: int = 189
WINDOW_WIDTH: int = 400
WINDOW_HEIGHT: int = 400

def second():
    window = Tk()
    window.title("Password Manager")
    window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, pady=20, padx=20)

    canvas = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    logo = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(IMAGE_WIDTH / 2 + WINDOW_WIDTH / 4, IMAGE_HEIGHT / 2, image=logo)
    canvas.grid(column=0, row=0)

    button = Button(window, text="click here")
    button.grid(column=1, row=0)
    window.mainloop()


def main():
    window = Tk()
    window.title("Password Manager")
    window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, pady=20, padx=20)

    canvas = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    logo = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(IMAGE_WIDTH / 2 + WINDOW_WIDTH /4, IMAGE_HEIGHT / 2, image=logo)
    canvas.grid(column=0, row=0)

    button = Button(window, text="click here", command=second)
    button.grid(column=1, row=0)
    window.mainloop()


if __name__ == '__main__':
    main()
