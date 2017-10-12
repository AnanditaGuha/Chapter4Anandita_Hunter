from turtle import Turtle, Screen

double = (2 ** 0.5) / 2

screen = Screen()

yay = Turtle()
yay.pencolor("blue")
yay.setheading(45)

for radius in range(20, 20 * 5 + 1, 20):
    yay.penup()
    yay.goto(radius/2, -radius/2)
    yay.pendown()
    yay.circle(radius * double, steps=4)

