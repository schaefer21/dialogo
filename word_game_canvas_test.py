# Description: This file is used to test the canvas for the word game
# and see if the new image cards (text+symbol) fit

from tkinter import *
import tkinter as tk
import tkinter.font as TkFont
from PIL import ImageTk,Image


title_pos_left = [50, 130]
text_pos_left = [50, 200]
title_game_pos_left = [190, 22]
score_pos_left = [50, 400]
shift = 800
shift_y = 40

img_pos = [[40, 80], [300, 80], [560, 80]]
rectangle_pos = [[240, 370], [500, 370], [760, 370]]

# master
root = Tk()
w0, h0 = 800, 480
w1, h1 = 800, 480

# hdmi0
win0 = tk.Toplevel(root)
win0.geometry(f"{w0}x{h0}+0+0")
win0.attributes("-fullscreen", True)

# hdmi1
win1 = tk.Toplevel(root)
win1.geometry(f"{w1}x{h1}+{w0}+0")
win1.attributes("-fullscreen", True)

root.withdraw()

bg_color = "#FEFEFE"

logo = ImageTk.PhotoImage(Image.open("logo.png").resize((169,60)))

# design variables
title_font = TkFont.Font(family='Segoe UI', size=32, weight='bold')
text_font = TkFont.Font(family = "Segoe UI", size = 20)
title_font_game = TkFont.Font(family="Segoe UI", size=20, weight="bold")
design_aspects = [logo, title_font, text_font, title_font_game]


# image
img_size = (406, 287) # changed size of image to be more wide
apple_img = ImageTk.PhotoImage(Image.open("imgs/word_game/full_cards_wide/apple.png").resize(img_size))
# initialize canvas
canvas = Canvas(win0, width = 1600, height = 480, bg = bg_color)
canvas1 = Canvas(win1, width = 1600, height = 480, bg = bg_color)
canvas.create_image(15, 15, anchor=NW, image=design_aspects[0]) # logo

# example of how to show canvas for word game
def canvas_word_game(left_or_right, canvas, design, image, score=[0,0]):
 
    if left_or_right == "left":
        # first display
        canvas.create_image(15, 15, anchor=NW, image=design[0]) # logo
        canvas.create_text(title_game_pos_left[0], title_game_pos_left[1], text = 'explainer of word game', anchor= NW, width=625, font = design[3])
        canvas.create_image(img_pos[1][0], img_pos[1][1], anchor=NW, image=image)


    elif left_or_right == "right":
        # second display
        # unsure what we want to display here
        canvas1.create_image(15, 15, anchor=NW, image=design[0]) # logo
        canvas1.create_text(title_game_pos_left[0], title_game_pos_left[1], text = 'guess the word', anchor= NW, width=625, font = design[3])

    
    canvas.create_text(score_pos_left[0], score_pos_left[1], text = str(score[0]) + " : " + str(score[1]), anchor= NW, width=625, font = design[2])


canvas.pack()
canvas1.pack()
canvas_word_game("left", canvas, design_aspects, apple_img, score=[1,2])
canvas_word_game("right", canvas1, design_aspects, apple_img, score=[1,2])

root.mainloop()