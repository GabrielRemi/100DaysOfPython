import os
import tkinter
from tkinter import Widget, Button, Label
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_WIDTH = 800
CARD_HEIGHT = 526
FONT = ("Ubuntu", 20, "normal")
KNOWN_LANGUAGE = "English"
GUESS_LANGUAGE = "French"
MY_CSV_FILE = "data/my_french_words.csv"


def font(size: int, font_type="normal") -> tuple:
    return FONT, size, font_type


root: tkinter.Tk = tkinter.Tk()
root.title("Test")
root.config(width=800, height=600, background=BACKGROUND_COLOR, padx=20, pady=20)

# Images
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")
right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

canvas: tkinter.Canvas = tkinter.Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, background=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
card_image = canvas.create_image(CARD_WIDTH, CARD_HEIGHT, image=card_front_img, anchor=tkinter.SE)
language_label = canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 2 - 80, text=KNOWN_LANGUAGE,
                                    anchor=tkinter.CENTER, font=font(28))
guess_word_label = canvas.create_text(CARD_WIDTH / 2, CARD_HEIGHT / 2, text="Text",
                                      anchor=tkinter.CENTER, font=font(35, "italic"))


class Card:
    def __init__(self):
        self.known_word = ""
        self.guess_word = ""
        self.guessed = False
        self.words = pandas.DataFrame()
        try:
            self.words = pandas.read_csv(MY_CSV_FILE)
        except FileNotFoundError:
            self.words = pandas.read_csv("data/french_words.csv")
        self.index = -1

    def change_word(self):
        self.index = random.randint(0, len(self.words) - 1)
        self.known_word = self.words.iloc[self.index]["English"]
        self.guess_word = self.words.iloc[self.index]["French"]

    def init(self):
        global root

        self.change_word()
        canvas.itemconfig(language_label, text=GUESS_LANGUAGE)
        canvas.itemconfig(card_image, image=card_front_img)
        canvas.itemconfig(guess_word_label, text=self.guess_word)

        root.after(3000, self.flip)

    def next_card(self, correct: bool):
        self.save()
        if correct:
            self.words.drop(index=self.index, inplace=True)
            self.words.reset_index(inplace=True, drop=True)

        self.init()

    def flip(self) -> None:
        if len(self.words) == 0:
            self.end_card()
            return
        global canvas, card_image, language_label, guess_word_label

        canvas.itemconfig(language_label, text=KNOWN_LANGUAGE)
        canvas.itemconfig(card_image, image=card_back_img)
        canvas.itemconfig(guess_word_label, text=self.known_word)

    def end_card(self):
        global canvas, language_label, guess_word_label
        canvas.itemconfig(language_label, text="")
        canvas.itemconfig(guess_word_label, text="You Guessed all Words correctly!", font=font(35, "bold italic"))

    def save(self):
        self.words.to_csv(path_or_buf=MY_CSV_FILE, index=False)


def main():
    global canvas, root

    card = Card()
    card.init()

    wrong_button = Button(root, text="red", image=wrong_img, background=BACKGROUND_COLOR,
                          command=lambda: card.next_card(False))
    right_button = Button(root, text="green", image=right_img, background=BACKGROUND_COLOR,
                          command=lambda: card.next_card(True))
    wrong_button.grid(row=1, column=1)
    right_button.grid(row=1, column=0)

    picture = Label(root, text="Picture", image=card_front_img, background=BACKGROUND_COLOR)
    canvas.grid(row=0, column=0, columnspan=2)

    root.mainloop()


if __name__ == "__main__":
    main()
