from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.width(2)

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clear():
    tim.reset()

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear)
screen.onkey(key="a",fun= move_left)
screen.onkey(key="d", fun= move_right)

screen.exitonclick()