# Simple snake game in python 3 or 2 
# Aplril 12 2021
# Part 1: the set up

import turtle
import time
import random

delay = 0.1

#Score!!!!!!!!!!!!!!!!!!!!!!!!!!!!
score = 0
high_score = 0

# Set up the screen
gameboard = turtle.Screen()
gameboard.title("Snake PARTY By reg5060")
gameboard.bgcolor("grey")
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
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score: 0  High Score: 0", align="center", font=("Lobster", 24, "normal"))

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

        # Reset the score 
        score = 0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Lobster", 24, "normal"))



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
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Lobster", 24, "normal"))


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