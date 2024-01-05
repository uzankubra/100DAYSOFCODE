from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data = pd.read_csv("words_to_learn.csv")

except FileNotFoundError:
    original_data=pd.read_csv("most_common_russian.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title, text="Russian", fill="black")
    canvas.itemconfig(card_word, text=current_card["ru"], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer= window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["en"], fill="white")
    canvas.itemconfig(card_background,image=back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data= pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("VocRus")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer= window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img=PhotoImage(file="images/card_back.png")
card_background= canvas.create_image(400, 263, image=front_img)
card_title= canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word= canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img=PhotoImage(file="images/wrong.png")
unknown_button=Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
known_button=Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()


