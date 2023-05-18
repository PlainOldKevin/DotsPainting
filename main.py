# Imports 
import turtle as t
import random as rand

# Create turtle
cursor = t.Turtle()
t.colormode(255)

# Function to select color for circle
def random_color():
    r = rand.randint(0, 255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r, g, b)

# Function to tell the cursor to draw 10 circles in a line
def draw():
    for _ in range(10):
        cursor.pendown()
        cursor.dot(20, random_color())
        cursor.penup()
        cursor.forward(50) 

# Function to tell the cursor to reposition


# Setting cursor to starting position
cursor.penup()
cursor.setpos(-225, -125)


# Create screen
screen = t.Screen()
screen.exitonclick()
