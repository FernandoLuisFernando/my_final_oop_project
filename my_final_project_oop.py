from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 1000
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3 
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    pass 

class Food:
    
    def

def next_turn():
    pass

def change_direction():
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()
window.title("snake game")
window.resizable(False, False)

score = 0 
direction = 'down'

label = Label(window, text='score:{}'.format(score), font=('consolas, 40'))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenwidth()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
 
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()
window.mainloop()