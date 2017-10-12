import turtle

def draw_poly(t, ss, sz):
    
    for i in range(ss):
        t.forward(sz)
        t.left(120)

def drawequitriangle(t, sz):
    draw_poly(t, 3, sz)
    
wn = turtle.Screen()




drawequitriangle(turtle, 100)