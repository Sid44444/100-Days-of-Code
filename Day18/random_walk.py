from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

screen = Screen()

tim.width(10)#line thickness set to 10

tim.speed ("fastest")

#centralise pen
tim.penup()
tim.goto(0,0)
tim.pendown()

#draw a random walk ( mathematical object). Thickness of line, speed up turtle, random colour and random direction

directions = [0, 90, 180, 270]#set directions as N,S,E and W

for _ in range (300): #set to draw 300 times
    tim.color(random_color())#uses the tuple to create random colours
    tim.forward(20)
    tim.setheading(random.choice(directions))#chooses a random direction

screen.exitonclick()