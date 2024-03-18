from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

default_file = "data/french_words.csv"
learn_file = "data/words_to_learn.csv"

try:
    data_check = pandas.read_csv(learn_file)
except FileNotFoundError:
    data = pandas.read_csv(default_file).to_dict(orient="records")
else:
    data = data_check.to_dict(orient="records")

current_card = {}


def save_progress():
    new_item = pandas.DataFrame(data)
    new_item.to_csv(learn_file, index=False)


def next_card():
    global data, current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(data)

    canvas.itemconfigure(title_text, text="French", fill="black")
    canvas.itemconfigure(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)

    window.after(3000, func=flip_card)


def is_known():
    data.remove(current_card)
    save_progress()
    next_card()


def flip_card():
    global current_card
    canvas.itemconfigure(title_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=current_card["English"], fill="white")

    canvas.itemconfig(canvas_image, image=card_back_image)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image((400, 263), image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

title_text = canvas.create_text((400, 150), font=("Ariel", 40, "italic"), text="")
word_text = canvas.create_text((400, 263), font=("Ariel", 60, "italic"), text="")

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, command=is_known, highlightthickness=0)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
