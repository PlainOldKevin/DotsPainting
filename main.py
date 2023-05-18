# Imports 
import turtle as t
import random as rand

# Create turtle
cursor = t.Turtle()
t.colormode(255)
cursor.hideturtle()

# Function to select color for circle
def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r, g, b)

# Function to tell the cursor to draw 10 circles in a line
def draw():
    # 10 circles
    for _ in range(10):
        # Choose random color
        color = random_color()
        # Pen down to draw
        cursor.pendown()
        # Choose pen color, fill color, draw circle, end fill
        cursor.pencolor(color)
        cursor.fillcolor(color)
        cursor.begin_fill()
        cursor.circle(10)
        cursor.end_fill()
        # Pen up to move forward 
        cursor.penup()
        # Move forward
        cursor.forward(50) 

# Function to tell the cursor to reposition
def reposition(start):
    cursor.setpos(start[0], cursor.ycor() + 40)

# Setting cursor to starting position
start = (-225, -125)
cursor.penup()
cursor.setpos(start)
cursor.speed("fastest")

# For loop to make functions work
for _ in range(10):
    draw()
    reposition(start)


# Create screen
screen = t.Screen()
screen.exitonclick()
