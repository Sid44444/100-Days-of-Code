from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")

colours = ["BlueViolet", "brown1", "cyan1", "DarkGoldenrod", "DarkOliveGreen1", "coral2", "DeepPink2"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen.exitonclick()