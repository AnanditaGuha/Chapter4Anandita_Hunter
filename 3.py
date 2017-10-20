import turtle
def draw_poly(t,n,sz):
    for i in range(n):
        t.forward(sz)
        t.right(360/n)
wn = turtle.Screen()
tess = turtle.Turtle()
wn.bgcolor("lightgreen")
tess.color("hotpink")
tess.pensize(3)
draw_poly(tess,8,50)