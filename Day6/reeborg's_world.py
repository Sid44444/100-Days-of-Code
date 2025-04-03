#https://reeborg.ca/reeborg.html
#hurdle challenges 1,2,3,4 completed. Using for statements and while loops.
#hurdle 4 challenge code below, errors do not appear in the webpage above.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()