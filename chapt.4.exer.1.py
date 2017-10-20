import turtle
def make_square(turt,length):
    for i in range(4):
        turt.forward(length)
        turt.left(360/4)
      #return turt.pos()
    
wn = turtle.Screen()
rob = turtle.Turtle()
wn.bgcolor("lightgreen")
rob.color("hotpink")
rob.pensize(3)
for i in range(5):
    make_square (rob, 20)
    rob.penup()
    rob.forward (40)
    rob.pendown()
    