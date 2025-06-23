from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
OBSTACLE_COLOR = "#808080"

score = 0 
high_score = 0
direction = 'down'
obstacle = []

def get_random_color():
        return f'#{random.randint(0, 0xFFFFFF):06x}'


def get_random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

def increases_difficulty():
    global SPEED
    if score % 5 == 0 and SPEED > 20:
        SPEED -= 5 
        print(f"Speed has increased")

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [[0, 0] for _ in range(BODY_PARTS)]
        self.squares = []

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

            if [x, y] not in snake.coordinates:
                break

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                           fill=FOOD_COLOR, tag="food")

def create_obstacle(count=5):
    global obstacles
    for blocks in range(count):
        while True:
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            if [x, y] not in snake.coordinates and [x, y] != food.coordinates:
                obstacles.append([x, y])
                canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                        fill=OBSTACLE_COLOR, tag="obstacle")
                break
                

def next_turn(snake):
    global food, score 
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE 
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if new_head == food.coordinates:
        score += 1 
        increases_difficulty()
        label.config(text=f"Score: {score} | High Score: {high_score}"))

    if x == food.coordinates[0] and y == food.coordinates[1]:
    
        score += 1
        label.config(text=f"score: {score}")

        canvas.delete("food") 
        food = Food()   

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions():
     game_over()
    else:

        window.after(SPEED, next_turn, snake)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != "up":
            direction = new_direction


def check_collisions():
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True
    
    if [x, y] in snake.coordinates[1:]:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='GAME OVER', fill='red', tag="GAME OVER")

window = Tk()
window.title("snake game")
window.resizable(False, False)
window.configure(bg=BACKGROUND_COLOR)

score = 0 
direction = 'down'

label = Label(window, text=f"score: {score}",font=('consolas', 40), bg=BACKGROUND_COLOR, fg="white")
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR,height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = GAME_WIDTH
window_height = GAME_HEIGHT 
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))


snake = Snake()
food = Food()
next_turn(snake)

window.mainloop()