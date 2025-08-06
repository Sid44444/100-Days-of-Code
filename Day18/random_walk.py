from turtle import Turtle, Screen
import turtle as t
import random

t = t.Turtle()
screen = Screen()

#line thickness set to 10
t.width(10)
#t.forward(300)

t.speed ("fastest")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#centralise pen
t.penup()
t.goto(0,0)
t.pendown()

#draw a random walk ( mathematical object). Thickness of line, speed up turtle,

#set directions as N,S,E and W
directions = [0, 90, 180, 270]

for _ in range (300): #set to draw 300 times
    t.color(random.choice(colours))
    t.forward(20)
    t.setheading(random.choice(directions))#chooses a random direction

screen.exitonclick()