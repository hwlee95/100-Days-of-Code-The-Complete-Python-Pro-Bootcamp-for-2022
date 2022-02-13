# Solving the maze from https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# turn_left(), front_is_clear(), right_is_clear(), move(), at_goal(), wall_in_front() is pre-defined in Reeborg's World

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if wall_in_front():
            turn_left()
            move()
        else:
            move()
