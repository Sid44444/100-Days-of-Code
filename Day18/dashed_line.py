from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("red")

tim.penup()
tim.goto(-300,0)
tim.pendown()

for _ in range(30):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen.exitonclick()