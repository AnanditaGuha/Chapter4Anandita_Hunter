import turtle
def draw_spiral(t,n,sz,ang):
    for i in range(n):
        t.right(ang)
        t.forward(sz)
        sz = sz + 5
wn = turtle.Screen()
tess = turtle.Turtle()
wn.bgcolor("lightgreen")
tess.color("blue")
tess.pensize(3)
draw_spiral(tess,99,5,89)
tess.right(90)