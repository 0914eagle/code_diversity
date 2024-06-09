
def get_button_presses(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    pushes = 0
    up_button_available = True
    down_button_available = True

    # Loop until the current floor is the goal floor or the elevator cannot move anymore
    while current_floor != goal and (up_button_available or down_button_available):
        # Check if the up button can be pressed
        if up_button_available and current_floor + up <= floors:
            current_floor += up
            pushes += 1
        # Check if the down button can be pressed
        elif down_button_available and current_floor - down >= 1:
            current_floor -= down
            pushes += 1
        # Check if the elevator cannot move anymore
        else:
            up_button_available = False
            down_button_available = False

    # Return the number of pushes or "use the stairs" if the elevator cannot reach the goal floor
    if current_floor == goal:
        return pushes
    else:
        return "use the stairs"

