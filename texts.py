from tkinter import *
from random import choice 
import tkinter as tk
import tkinter.font as TkFont
from PIL import ImageTk,Image

##################################################################
# VARIABLES
##################################################################

bg_color = "#FFFFFF"
title_pos_left = [50, 130]
text_pos_left = [50, 200]
title_game_pos_left = [190, 22]
score_pos_left = [50, 430]
shift = 800
shift_y = 40

##################################################################
# FUNCTIONS
##################################################################
img_pos = [[40, 100], [300, 100], [560, 100]]
rectangle_pos = [[240, 390], [500, 390], [760, 390]]

def canvas_expl(canvas, title, subtitle, design):
    canvas.delete("all")
    canvas.create_image(15, 15, anchor=NW, image=design[0])
    canvas.create_text(title_pos_left[0], title_pos_left[1], text = title, anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0], text_pos_left[1], text = subtitle, anchor= NW, width=625, font = design[2])
     # line
    canvas.create_line(800, 0, 800, 480, fill="black", width = 2)
    # right display
    canvas.create_image(15 + shift, 15, anchor=NW, image=design[0])
    canvas.create_text(title_pos_left[0] + shift, title_pos_left[1], text = title, anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1], text = subtitle, anchor= NW, width=625, font = design[2])
    # pack
    canvas.pack()

def canvas_expl_two_disp(canvas, texts, design):
    canvas.delete("all")
    canvas.create_image(15, 15, anchor=NW, image=design[0])
    canvas.create_text(title_pos_left[0], title_pos_left[1], text = texts[0], anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0], text_pos_left[1], text = texts[1], anchor= NW, width=625, font = design[2])
    # line
    canvas.create_line(800, 0, 800, 480, fill="black", width = 2)
    # right display
    canvas.create_image(15 + shift, 15, anchor=NW, image=design[0])
    canvas.create_text(title_pos_left[0] + shift, title_pos_left[1], text = texts[2], anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1], text = texts[3], anchor= NW, width=625, font = design[2])
    # pack
    canvas.pack()

def canvas_img_game(canvas, texts, design, imgs, correct_img_id, score):
    """ input: canvas, texts(two titles), design(logo, title_font, text_font, title_font_game), imgs(list of image_triples)
        creates game screen from which to guess the images
    """
    # choose images set randomly
    #image_set = imgs[sets_used % len(imgs)]
    image_set = choice(imgs)

    # clear canvas
    canvas.delete("all")
    
    # first display
    canvas.create_image(15, 15, anchor=NW, image=design[0]) # logo
    canvas.create_text(title_game_pos_left[0], title_game_pos_left[1], text = texts[0], anchor= NW, width=625, font = design[3]) # title
    canvas.create_image(img_pos[0][0], img_pos[0][1], anchor=NW, image=image_set[0])
    canvas.create_image(img_pos[1][0], img_pos[1][1], anchor=NW, image=image_set[1])
    canvas.create_image(img_pos[2][0], img_pos[2][1], anchor=NW, image=image_set[2])
    canvas.create_rectangle(img_pos[correct_img_id][0] - 5, img_pos[correct_img_id][1] - 5, rectangle_pos[correct_img_id][0] + 4, rectangle_pos[correct_img_id][1] + 4, width = 5, outline = "green")
    canvas.create_text(img_pos[0][0] + 100, img_pos[0][1] + 310, text = "A", font = design[2])
    canvas.create_text(img_pos[1][0] + 100, img_pos[1][1] + 310, text = "B", font = design[2])
    canvas.create_text(img_pos[2][0] + 100, img_pos[2][1] + 310, text = "C", font = design[2])

    # separation line
    canvas.create_line(800, 0, 800, 480, fill="black", width = 2)

    # second display
    canvas.create_image(15 + shift, 15, anchor=NW, image=design[0])
    canvas.create_text(title_game_pos_left[0] + shift, title_game_pos_left[1], text = texts[1], anchor= NW, width=625, font = design[3])
    canvas.create_image(img_pos[0][0] + shift, img_pos[0][1], anchor=NW, image=image_set[0])
    canvas.create_image(img_pos[1][0] + shift, img_pos[1][1], anchor=NW, image=image_set[1])
    canvas.create_image(img_pos[2][0] + shift, img_pos[2][1], anchor=NW, image=image_set[2])
    canvas.create_text(img_pos[0][0] + 100 + shift, img_pos[0][1] + 310, text = "A", font = design[2])
    canvas.create_text(img_pos[1][0] + 100 + shift, img_pos[1][1] + 310, text = "B", font = design[2])
    canvas.create_text(img_pos[2][0] + 100 + shift, img_pos[2][1] + 310, text = "C", font = design[2])
    
    # score
    canvas.create_text(score_pos_left[0], score_pos_left[1], text = str(score[0]) + " : " + str(score[1]), anchor= NW, width=625, font = design[2])
    canvas.create_text(score_pos_left[0] + shift, score_pos_left[1], text = str(score[0]) + " : " + str(score[1]), anchor= NW, width=625, font = design[2])
    
    # pack
    canvas.pack()

def canvas_expl_buttons():
    print()

def canvas_hand_over(canvas, texts, design, score_of_round):
    canvas.delete("all")
    canvas.create_image(15, 15, anchor=NW, image=design[0])
    canvas.create_text(title_pos_left[0], title_pos_left[1], text = texts[0], anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0], text_pos_left[1], text = texts[1] + str(score_of_round) + texts[2], anchor= NW, width=625, font = design[2])
    canvas.create_text(text_pos_left[0], text_pos_left[1] + shift_y, text = texts[3], anchor= NW, width=625, font = design[2])
    canvas.create_text(text_pos_left[0], text_pos_left[1] + shift_y * 2, text = texts[4], anchor= NW, width=625, font = design[2])

     # line
    canvas.create_line(800, 0, 800, 480, fill="black", width = 2)
    # right display
    canvas.create_image(15 + shift, 15, anchor=NW, image=design[0])
    canvas.create_text(title_pos_left[0] + shift, title_pos_left[1], text = texts[0], anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1], text = texts[1] + str(score_of_round) + texts[2], anchor= NW, width=625, font = design[2])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1] + shift_y, text = texts[3], anchor= NW, width=625, font = design[2])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1] + shift_y * 2, text = texts[4], anchor= NW, width=625, font = design[2])
    # pack
    canvas.pack()

def canvas_end_slide(canvas, texts, design, score):
    # clear canvas
    canvas.delete("all")    

    # first display
    canvas.create_image(15, 15, anchor=NW, image=design[0]) # logo
    canvas.create_text(title_pos_left[0], title_pos_left[1], text = texts[0], anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0], text_pos_left[1], text = texts[1] + str(score[0]) + " Punkte.", anchor= NW, width=625, font = design[2])
    canvas.create_text(text_pos_left[0], text_pos_left[1] + shift_y, text = texts[2] + str(score[1]) + " Punkte.", anchor= NW, width=625, font = design[2])
    
    # separation line
    canvas.create_line(800, 0, 800, 480, fill="black", width = 2)

    # second display
    canvas.create_image(15 + shift, 15, anchor=NW, image=design[0]) #logo
    canvas.create_text(title_pos_left[0] + shift, title_pos_left[1], text = texts[0], anchor= NW, width=625, font = design[1])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1], text = texts[1] + str(score[0]) + " Punkte.", anchor= NW, width=625, font = design[2])
    canvas.create_text(text_pos_left[0] + shift, text_pos_left[1] + shift_y, text = texts[2] + str(score[1]) + " Punkte.", anchor= NW, width=625, font = design[2])

    # score
    if score[0] != score[1]:
        canvas.create_text(text_pos_left[0], text_pos_left[1] + shift_y * 2, text = texts[3] + str(1 if score[0]>score[1] else 2)  + "!", anchor= NW, width=625, font = design[2])
        canvas.create_text(text_pos_left[0] + shift, text_pos_left[1] + shift_y * 2, text = texts[3] + str(1 if score[0]>score[1] else 2) + "!", anchor= NW, width=625, font = design[2])
    else:
        canvas.create_text(text_pos_left[0], text_pos_left[1] + shift_y * 2, text = "Es ist Unentschieden!", anchor= NW, width=625, font = design[2])
        canvas.create_text(text_pos_left[0] + shift, text_pos_left[1] + shift_y * 2, text = "Es ist Unentschieden!", anchor= NW, width=625, font = design[2])

    # pack
    canvas.pack()

    
##################################################################
# TEXTS
##################################################################

texts_stage_0 = {
    "start_frame": ["Dialogo",
                    "Sprechen lehrt sprechen!"],
    "explanation": ["Kurze Erklärung:",
                    "In diesem Spiel könnt ihr einfach Deutsch Sprechen üben. Es gibt verschiedene kleine Spiele. Dabei seid ihr in zwei Gruppen aufgeteilt und in jeder Gruppe gibt es in jeder Runde einen Erklärer."],
    "explanation_of_buttons": ["Was machen die Knöpfe?",
                    "Jedes Spiel hat mehrere Aufgaben."],
    "group_building": ["Zuerst: Gruppen bilden!",
                    "Teilt euch in zwei Gruppen auf, sodass die Gruppen ungefähr gleich groß sind. Entscheidet, wer in Gruppe 1 und wer in Gruppe 2 ist. "],
    "first_group_starts": ["Gruppe 1 fängt an!",
                    "Wählt eine Person aus eurer Gruppe, die erklärt. Diese bekommt die Dialogo Box."],
    "the_game_is": ["Das Spiel heißt: Bilder raten!",
                    "Eine Person beschreibt eins von drei Bildern, die anderen müssen raten, welches das Richtige ist. Ihr habt eine Minute Zeit. Ihr müsst so viele Bilder erraten, wie möglich!"]
}

texts_stage_1 = {
    "guesser_and_explainer": ["Du erklärst!",
                    "Es wird gleich das Spiel angezeigt. Dafür sollst nur du diese Seite der Dialogo Box sehen.",
                    "Ihr müsst raten!",
                    "Die Person mit der Box beschreibt gleich die Bilder. Ihr müsst sagen, was richtig ist!"],
    "image_game": ["Beschreibe das markierte Bild!",
                    "Ratet, welches Bild das Richtige ist!"]
}

texts_stage_2 = {
    "other_team_turn": ["Eure Zeit ist um!",
                    "Ihr habt ",
                    " Punkte bekommen.",
                    "Jetzt ist das andere Team dran.",
                    "Gibt das Dialogo dem anderen Team :)"]
}

texts_stage_3 = {
    "end_screen": ["Das Spiel ist vorbei!",
                    "Gruppe 1 hat ",
                    "Gruppe 2 hat ", 
                    "Glückwunsch an Gruppe "]
}

# Stage 0
#### start_frame
#### explanation
#### explanation_of_buttons
#### group_building
#### first_group_starts
#### the_game_is
# Stage 1
#### guesser_and_explainer
#### image_game
# Stage 2
#### other_team_turn
# Stage 3
#### end_screen
