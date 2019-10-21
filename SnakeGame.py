# Snake Game Using Turtle

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake game by Fatemah")
window.bgcolor("black")
window.setup(width = 600, height = 600)
# Turns off the screen updates
window.tracer(0)

# Create Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#4B4342")
head.penup()
head.setpos(0, 0)
head.direction = "stop"

# Create Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.setpos(0, 100)

# Create the Snake Body using a list
segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.setpos(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Game over
end_game = turtle.Turtle()
end_game.speed(0)
end_game.shape("square")
end_game.color("red")
end_game.penup()
end_game.hideturtle()
end_game.setpos(0, 0)

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"        

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)     

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "8")
window.onkeypress(go_down, "2")
window.onkeypress(go_left, "4")
window.onkeypress(go_right, "6")

# Main game loop
while True:
    window.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.setpos(0, 0)
        head.direction = "stop"

        end_game.write("Game Over!!", align="center", font=("Courier", 30, "normal"))

        # Hide the segments
        for segment in segments:
            segment.setpos(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the Score
        score = 0

        # Reset the delay
        delay = 1

        # Update the score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        end_game.clear()

    # Check for collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.setpos(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0) # Animation Speed
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10
        
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].setpos(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].setpos(x, y)        

    move()

    # Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.setpos(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.setpos(1000, 1000)

            # Clear the segments list
            segments.clear()    

    time.sleep(delay)


window.mainloop()
