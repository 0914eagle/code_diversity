
def elevator_buttons(floors, start, goal, up, down):
    # Initialize variables
    current_floor = start
    pushes = 0
    up_pushes = 0
    down_pushes = 0

    # Loop until the goal floor is reached
    while current_floor != goal:
        # Check if the up button can be pressed
        if current_floor + up <= floors:
            current_floor += up
            up_pushes += 1
        # Check if the down button can be pressed
        elif current_floor - down >= 1:
            current_floor -= down
            down_pushes += 1
        # If neither button can be pressed, return "use the stairs"
        else:
            return "use the stairs"
        pushes += 1

    # Return the total number of pushes
    return pushes

