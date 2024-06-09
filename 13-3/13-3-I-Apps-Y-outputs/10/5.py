
def elevator_buttons(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    pushes = 0
    up_button_available = True
    down_button_available = True

    # Loop until the goal floor is reached or the elevator cannot reach the goal floor
    while current_floor != goal and (up_button_available or down_button_available):
        # Check if the up button can be used
        if up_button_available and current_floor + up <= floors:
            current_floor += up
            pushes += 1
        # Check if the down button can be used
        elif down_button_available and current_floor - down >= 1:
            current_floor -= down
            pushes += 1
        # Check if the elevator cannot reach the goal floor
        else:
            return "use the stairs"

    # Return the number of pushes required to reach the goal floor
    return pushes

