import emoji
import os
import tkinter
from tkinter import Tk, Canvas, Button, Label

LONG_BREAK: int = 300
SHORT_BREAK: int = 3
WORK_TIME: int = 10
FONT: str = "Arial"
FONT_BIG: int = 24
FONT_SMALL: int = 15
MAX_REPS = 3

timer_loop: str | None = None


def font(*args) -> tuple:
    return FONT, *args


is_work_time = True
reps: int = 0


def format_time(seconds: int) -> str:
    minutes = int(seconds / 60)
    seconds = seconds - minutes * 60

    return "{:02d}".format(minutes) + ":" + "{:02d}".format(seconds)


def main():
    print(os.getcwd())
    window: Tk = Tk()

    window.title("Pomodoro")
    window.config(padx=30, pady=30)

    canvas = Canvas(window, width=250, height=280)
    tomato_img = tkinter.PhotoImage(file="tomato.png")
    canvas.create_image(125, 140, image=tomato_img)
    timer_text = canvas.create_text(125, 165, text="00:00", font=font(FONT_BIG), fill="white")
    canvas.grid(row=1, column=1)

    interval_label: Label = Label(window, text="", font=font(FONT_SMALL))
    interval_label.grid(row=2, column=1)

    timer_label = Label(window, text="Timer", font=font(FONT_BIG), fg="green")
    timer_label.grid(row=0, column=1)

    def timer(time: int) -> None:
        global reps, is_work_time, timer_loop
        nonlocal timer_text, canvas, interval_label, timer_label
        canvas.itemconfig(timer_text, text=format_time(time))

        if time == 0:
            is_work_time = not is_work_time
            if is_work_time:
                time = WORK_TIME
                timer_label.config(text="Work", fg="green", font=font(FONT_BIG))
            else:
                reps += 1
                interval_label.config(text=str(emoji.emojize(":check_mark_button:" * reps)))
                timer_label.config(text="Break", fg="red", font=font(FONT_BIG))
                time = SHORT_BREAK

            if reps == MAX_REPS:
                return
        timer_loop = window.after(1000, timer, time - 1)

    start_button = Button(window, text="Start", font=font(FONT_SMALL), command=lambda: timer(WORK_TIME))
    start_button.grid(row=2, column=0)

    def reset():
        global reps, timer_loop
        nonlocal canvas, timer_text, window
        if timer:
            window.after_cancel(timer_loop)
        reps = 0
        canvas.itemconfig(timer_text, text="")

    reset_button = Button(window, text="Reset", font=font(FONT_SMALL), command=reset)
    reset_button.grid(row=2, column=2)

    window.mainloop()


if __name__ == "__main__":
    main()
