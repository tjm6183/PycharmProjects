from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# create window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create canvas, add front image
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))

# configure background color, start grid
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# read data from CSV- create list for spent words
data = pandas.read_csv("data/french_words.csv")
all_words = data.French.to_list()
guessed_words = []

# Pull a random French word
canvas.create_text(400, 263, text=random.choice(all_words), font=("Ariel", 60, "bold"))

# Add the images here
red_image = PhotoImage(file="images/wrong.png")
green_image = PhotoImage(file="images/right.png")

# Creates the red button
red_button = Button(image=red_image, highlightthickness=0)
red_button.grid(row=1, column=0)

# Creates the green button
green_button = Button(image=green_image, highlightthickness=0)
green_button.grid(row=1, column=1)






window.mainloop()