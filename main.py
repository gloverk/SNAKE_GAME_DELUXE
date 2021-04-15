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
gameboard.bgcolor("red")
gameboard.setup(width=600, height=600)
gameboard.tracer(0)

# Snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle")
snake.color("black")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("grey")
food.penup()
food.goto(0,100)

segments = []

# Function
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
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

    # Check for a collision with the border
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()


    #check for collision with the food
    if snake.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)

    #Move the end segments first in reverse open
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move segment 0 to where the snake is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x,y)

    move()

    # Check for a collision with the body segments
    for segment in segments:
        if segment.distance(snake) <20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

    time.sleep(delay)

gameboard.mainloop()