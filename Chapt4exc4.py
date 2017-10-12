
import turtle

def draw_square(yay):
    for i in range(4):
        yay.forward(100)
        yay.right(90)

def draw():        
   
    window = turtle.Screen()
   
    bing = turtle.Turtle()
    bing.shape("turtle")      
    bing.color("blue")      
    bing.speed(0)             

    
    for i in range (30):
        draw_square(bing)
        bing.right(15)

   
draw()