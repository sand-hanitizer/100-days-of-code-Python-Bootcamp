#my solution for the maze problem
#it i believe is one of the clankiest ways to get it done
#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right() and front_is_clear():
        move()
    elif wall_on_right():
        while not front_is_clear():
            turn_left()
        move()
    elif front_is_clear():
        move()