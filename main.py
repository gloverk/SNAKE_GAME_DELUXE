# Simple snake game in python 3 or 2 
# Aplril 12 2021
# Part 1: the set up

import turtle
import time
import random

delay = 0.1

# Set up the screen
gameboard = turtle.Screen()
gameboard.title("Snake PARTY By reg5060")
gameboard.bgcolor("blue")
gameboard.setup(width=600, height=600)
gameboard.tracer(0)

# Snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("brown")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#Food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


# Functions
def go_up():
    snake.direction = "up"

def go_down():
    snake.direction = "down"

def go_left():
    snake.direction = "left"

def go_right():
    snake.direction = "right"

def move():
    if snake.direction == "up":
      y = snake.ycor()
      snake.sety(y + 20)

    if snake.direction == "down":
      y = snake.ycor()
      snake.sety(y - 20)

    if snake.direction == "left":
      x = snake.xcor()
      snake.setx(x - 20)

    if snake.direction == "right":
      x = snake.xcor()
      snake.setx(x + 20)

#Keyboard bindings
gameboard.listen()
gameboard.onkeypress(go_up, "Up")
gameboard.onkeypress(go_right, "Right")
gameboard.onkeypress(go_left, "Left")
gameboard.onkeypress(go_down, "Down")

# Main game loop
while True:
    gameboard.update()

    if snake.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

    move()

    time.sleep(delay)

gameboard.mainloop()