from tkinter import *
from time import sleep 
import random
import tkinter as tk
import tkinter.font as TkFont
from PIL import ImageTk,Image
from texts import create_canvas, create_canvas_2_disp, create_canvas_img, texts_stage_0, texts_stage_1, texts_stage_2, texts_stage_3, bg_color

# master
master = Tk()
master.geometry("1600x480") # pixels
master.title("Dialogo")

# import images
logo = ImageTk.PhotoImage(Image.open("logo.png").resize((169,60)))
tree = [ImageTk.PhotoImage(Image.open("imgs/tree1.png").resize((200, 290))),
        ImageTk.PhotoImage(Image.open("imgs/tree2.png").resize((200, 290))),
        ImageTk.PhotoImage(Image.open("imgs/tree3.png").resize((200, 290)))]
imgs = [tree] # can be used to pick randomly from the image sets

# design variables
title_font = TkFont.Font(family='Segoe UI', size=32, weight='bold')
text_font = TkFont.Font(family = "Segoe UI", size = 20)
title_font_game = TkFont.Font(family="Segoe UI", size=20, weight="bold")
design_aspects = [logo, title_font, text_font, title_font_game]

# logic variables
stage = 1 # {0, 1, 2, 3} as the stages
explanation_stage = 0 # {0, ...} as the explanations stages
task_stage = 0 # which images are shown
max_rounds = 3
round_counter = 0

# initialize canvas
canvas = Canvas(master, width = 1600, height = 480, bg = bg_color)

# WHILE LOOP 
button_clicked = True

if stage == 0:
    print("stage0")
    # START FRAME
    create_canvas(canvas, texts_stage_0["start_frame"][0], texts_stage_0["start_frame"][1], design_aspects)
    # EXPLANATION
    if button_clicked == True: ## CHANGE WITH BUTTON FUNCTIONALITY
        create_canvas(canvas, texts_stage_0["explanation"][0], texts_stage_0["explanation"][1], design_aspects)
        sleep(1)
        # EXPLANATION OF BUTTONS
        if button_clicked == True: ## CHANGE WITH BUTTON FUNCTIONALITY
            create_canvas(canvas, texts_stage_0["explanation_of_buttons"][0], texts_stage_0["explanation_of_buttons"][1], design_aspects)
            sleep(1)
            # GROUP BUILDING
            if button_clicked == True: ## CHANGE WITH BUTTON FUNCTIONALITY:
                create_canvas(canvas, texts_stage_0["group_building"][0], texts_stage_0["group_building"][1], design_aspects)
                sleep(1)
                ## FIRST GROUP STARTS
                if button_clicked == True: ## CHANGE WITH BUTTON FUNCTIONALITY:
                    create_canvas(canvas, texts_stage_0["first_group_starts"][0], texts_stage_0["first_group_starts"][1], design_aspects)
                    sleep(1)
                    ## THE GAME IS
                    if button_clicked == True: ## CHANGE WITH BUTTON FUNCTIONALITY:
                        create_canvas(canvas, texts_stage_0["the_game_is"][0], texts_stage_0["the_game_is"][1], design_aspects)
                        sleep(1)

# GAME STAGE
if stage == 1:
    print("stage1")
    #choose a random id for the correct image
    id = random.randint(0,2)
    create_canvas_2_disp(canvas, texts_stage_1["guesser_and_explainer"], design_aspects)
    # CHANGE WITH BUTTON FUNCTIONALITY
    create_canvas_img(canvas, texts_stage_1["image_game"], design_aspects, imgs, id)
    
# HAND OVER STAGE
if stage == 2:
    print("stage2")
    

# END STAGE
if stage == 3:
    print("stage3")

# UPDATE THE WINDOW
master.mainloop()

