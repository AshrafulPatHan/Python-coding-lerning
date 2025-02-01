import turtle
import math

# Setup the turtle
screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.speed(0)
flower.color("red")

def draw_petal():
    for _ in range(2):
        flower.circle(100, 60)  # Outer curve
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)

def draw_flower():
    for _ in range(6):  # 6 petals
        draw_petal()
        flower.right(60)  # Rotate for next petal

def draw_stem():
    flower.color("green")
    flower.right(90)
    flower.forward(200)

def draw_leaf():
    flower.color("dark green")
    flower.right(45)
    for _ in range(2):
        flower.circle(50, 90)
        flower.right(90)

# Draw the flower
draw_flower()

# Move to draw stem
flower.penup()
flower.goto(0, -50)
flower.pendown()
draw_stem()

# Move to draw leaves
flower.penup()
flower.goto(50, -150)
flower.pendown()
draw_leaf()

flower.penup()
flower.goto(-50, -180)
flower.pendown()
draw_leaf()

flower.hideturtle()
turtle.done()
