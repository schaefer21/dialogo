from tkinter import *
import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep
import time
import threading
import random
import tkinter.font as TkFont
from PIL import ImageTk,Image
from texts import canvas_img_game, canvas_expl_two_disp, canvas_expl, canvas_hand_over, canvas_expl_buttons, canvas_end_slide, texts_stage_0, texts_stage_1, texts_stage_2, texts_stage_3, bg_color

# master
master = Tk()
master.geometry("1600x480") # pixels
master.title("Dialogo")

# import images
img_size = (200, 290)
logo = ImageTk.PhotoImage(Image.open("logo.png").resize((169,60)))
tree = [ImageTk.PhotoImage(Image.open("imgs/tree/tree1.png").resize(img_size)),
        ImageTk.PhotoImage(Image.open("imgs/tree/tree2.png").resize(img_size)),
        ImageTk.PhotoImage(Image.open("imgs/tree/tree3.png").resize(img_size))]
sun = [ImageTk.PhotoImage(Image.open("imgs/sun/sun1.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/sun/sun2.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/sun/sun3.png").resize(img_size))]
dog = [ImageTk.PhotoImage(Image.open("imgs/dog/dog1.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/dog/dog2.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/dog/dog3.png").resize(img_size))]
fish = [ImageTk.PhotoImage(Image.open("imgs/fish/fish1.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/fish/fish2.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/fish/fish3.png").resize(img_size))]
flower = [ImageTk.PhotoImage(Image.open("imgs/flower/flower1.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/flower/flower2.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/flower/flower3.png").resize(img_size))]
house = [ImageTk.PhotoImage(Image.open("imgs/house/house1.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/house/house2.png").resize(img_size)),
       ImageTk.PhotoImage(Image.open("imgs/house/house3.png").resize(img_size))]
imgs = [tree, sun, dog, fish, flower, house] # can be used to pick randomly from the image sets
shuffle_imgs = []

# design variables
title_font = TkFont.Font(family='Segoe UI', size=32, weight='bold')
text_font = TkFont.Font(family = "Segoe UI", size = 20)
title_font_game = TkFont.Font(family="Segoe UI", size=20, weight="bold")
design_aspects = [logo, title_font, text_font, title_font_game]

# initialize canvas
canvas = Canvas(master, width = 1600, height = 480, bg = bg_color)

# button variables
button_right = 12 # GREEN
button_continue = 13 # WHITE
button_wrong = 21 # RED
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_right, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_continue, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(button_wrong, GPIO.IN, pull_up_down = GPIO.PUD_UP)
right_last = GPIO.HIGH
wrong_last = GPIO.HIGH
continue_last = GPIO.HIGH

# logic variables
stage = 0 # {0, 1, 2} as the stages
explanation_stage = 0 # {0, ...} as the explanations stages
task_stage = 0 # which images are shown

# game variables
rounds = 2 # even number so that every tea has same amount of rounds
round_time = 10.00 #round time in seconds
team = 1 # or 2
score = [0,0]
#sets_used = 0
sec = 0
timer_style = 0 # 0 or 1,  0...text timer 1...red circle timer

def add_score():
    score[team - 1] += 1
# GPIO.add_event_detect(button_right, GPIO.RISING, callback= add_score)

def next_task(): #functionality for getting new task
    correct_img_id = random.randint(0,2)
    canvas_img_game(canvas, texts_stage_1["image_game"], design_aspects, shuffle_imgs, correct_img_id, score)
    # sets_used += 1
    #print(sets_used)
    print("next task")

def update_timer(sec_left):
    if(timer_style == 1): # red circle timer  
        extend = int(360 / round_time * (sec))
        canvas.create_arc(730, 10, 790, 70, start=0, extent=extend, fill="red", outline= "red" )
    else: # text
        canvas.create_rectangle(730, 60, 790 , 30, fill = "white" , outline = "white")
        canvas.create_text(750, 30, text = str(sec_left), anchor= NW, width=625, font = design_aspects[3])
    canvas.pack
    
while True:

    # shuffle imgs
    shuffle_imgs = imgs
    random.shuffle(shuffle_imgs)

    print("stage 0")
    # EXPLANATION STAGE
    while (stage == 0):

        # START FRAME
        canvas_expl(canvas, texts_stage_0["start_frame"][0], texts_stage_0["start_frame"][1], design_aspects)

        # EXPLANATION
        if explanation_stage == 1:
            canvas_expl(canvas, texts_stage_0["explanation"][0], texts_stage_0["explanation"][1], design_aspects)
        if explanation_stage == 2:
            canvas_expl(canvas, texts_stage_0["explanation_of_buttons"][0], texts_stage_0["explanation_of_buttons"][1], design_aspects)
        if explanation_stage == 3:
            canvas_expl(canvas, texts_stage_0["group_building"][0], texts_stage_0["group_building"][1], design_aspects)
        if explanation_stage == 4:
            canvas_expl(canvas, texts_stage_0["first_group_starts"][0], texts_stage_0["first_group_starts"][1], design_aspects)
        if explanation_stage == 5:
            canvas_expl(canvas, texts_stage_0["the_game_is"][0], texts_stage_0["the_game_is"][1], design_aspects)
        if explanation_stage == 6:
            canvas_expl_two_disp(canvas, texts_stage_1["guesser_and_explainer"], design_aspects)
        if explanation_stage == 7:
            canvas.delete("all")
            explanation_stage = -1 #for transition - should be in last stage

        #transision to next stage after last explaination
        if explanation_stage == -1:
            stage = 1 #game stage
            team = 1
            score = [0,0]
            explanation_stage = 0

         # button check
        if continue_last == GPIO.LOW and GPIO.input(button_continue) == GPIO.HIGH:
            explanation_stage += 1
            print("continue")
        continue_last = GPIO.input(button_continue)

        # UPDATE THE WINDOW
        master.update()


    # GAME STAGE
    while stage == 1:
        print("stage 1 - game Stage")
         # set first task
        next_task()

        # visual timer
        # canvas.create_arc(730, 10, 790, 70, start=0, extent= 359.99, width = 3, fill="white", outline= "red" )
        canvas.pack

        # set timer
        guessing_time = round_time
        alarm = time.time() + guessing_time
        last_time = int(time.time())
        sec = 0
        # set button logic
        right_last = GPIO.HIGH
        wrong_last = GPIO.HIGH
        continue_last = GPIO.HIGH

        #-----game loop------
        while True:
            current_time = time.time()
            if current_time <= alarm:
                print(round(alarm - current_time))
                # print(str(int(time.time() % 100)))
                
                # button_right clicked
                if right_last == GPIO.LOW and GPIO.input(button_right) == GPIO.HIGH:
                    add_score()
                    next_task()
                    update_timer(int(alarm - current_time))
                    
                # wrong button clicked
                if wrong_last == GPIO.LOW and GPIO.input(button_wrong) == GPIO.HIGH:
                    next_task()
                    update_timer(int(alarm - current_time))
                    
                # continue button clicked
                if continue_last == GPIO.LOW and GPIO.input(button_continue) == GPIO.HIGH:
                    next_task()
                    update_timer(int(alarm - current_time))
                    
                # update button logic for next frame
                right_last = GPIO.input(button_right)
                wrong_last = GPIO.input(button_wrong)
                continue_last = GPIO.input(button_continue)

               
               # update visual timer each second 
                if(last_time < int(current_time)):
                    print("here")
                    sec += 1
                    update_timer(int(alarm - current_time))                  
                last_time = int(current_time)
                
                # iterator = 0
                # if (round(current_time) == round(alarm - (round_time/6 * (6-iterator)))):
                #   canvas.create_rectangle(100 + 100* iterator, 100, 200, 200, width = 5, outline = "green")
                #   canvas.pack()
                #   print("here")
                #   iterator += 1

            else:
                print("Time's up!")
                break
            sleep(0.10)
            # UPDATE THE WINDOW
            master.update()
        # -----game loop done-----

        # update rounds
        rounds -= 1

        # switch to hand over stage
        stage = 2
        print(score)
        # reset buttons
        right_last = GPIO.HIGH
        wrong_last = GPIO.HIGH
        continue_last = GPIO.HIGH


    # HAND OVER STAGE
    while stage == 2:
        print("stage 2")
        score_of_round = score[team-1]

        #include canvas for hand over here with scores
        canvas_hand_over(canvas, texts_stage_2["other_team_turn"], design_aspects, score_of_round)

        if continue_last == GPIO.LOW and GPIO.input(button_continue) == GPIO.HIGH:
            # change team
            if (team == 1):
                team = 2
            else:
                team = 1

            #transfer to right stage
            if rounds > 0:
                stage = 1 # game stage
            elif rounds == 0:
                stage = 3 # final stage
                continue_last = GPIO.HIGH

        continue_last = GPIO.input(button_continue)
        # UPDATE THE WINDOW
        master.update()

    # FINAL STAGE
    while stage == 3:
        print("stage 3")
        # SHOWING GAME RESULTS
        canvas_end_slide(canvas, texts_stage_3["end_screen"], design_aspects, score)
        # show final screen canvas here

        # transfer to stage 0 again
        if continue_last == GPIO.LOW and GPIO.input(button_continue) == GPIO.HIGH:
            stage = 0
            score = [0,0]
            right_last = GPIO.HIGH
            wrong_last = GPIO.HIGH
            continue_last = GPIO.HIGH
            stage = 0 # {0, 1, 2} as the stages
            explanation_stage = 0 # {0, ...} as the explanations stages
            task_stage = 0 # which images are shown
            rounds = 4
            team = 1

        continue_last = GPIO.input(button_continue)
        # UPDATE THE WINDOW
        master.update()



