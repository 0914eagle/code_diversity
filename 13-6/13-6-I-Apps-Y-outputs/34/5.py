
def get_button_presses(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    pushes = 0
    up_button_available = True
    down_button_available = True

    # Loop until we reach the goal floor or exceed the number of floors
    while current_floor != goal and current_floor <= floors:
        # Check if we can use the up button
        if up_button_available and current_floor + up <= floors:
            current_floor += up
            pushes += 1
            up_button_available = False
        # Check if we can use the down button
        elif down_button_available and current_floor - down >= 1:
            current_floor -= down
            pushes += 1
            down_button_available = False
        # We are unable to use either button, so we must use the stairs
        else:
            return "use the stairs"

    # Return the number of pushes required to reach the goal floor
    return pushes

