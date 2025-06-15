from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("chartreuse1")
my_screen = Screen()
print(my_screen.canvheight)


from random import random

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    timmy.right(angle)
    timmy.fd(steps)

my_screen.exitonclick()