#from turtle import Turtle, Screen
import turtle as t
#import Scrren
import random

tim = t.Turtle()
#screen = Screen()
tim.shape("classic")

tim.speed ("fastest")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap): #draws circle/s. num=size of gap
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.left(size_of_gap)# or tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()