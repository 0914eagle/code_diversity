
def get_button_pushes(f, s, g, u, d):
    # Initialize variables
    pushes = 0
    current_floor = s

    # Loop until we reach the goal floor or exceed the number of floors
    while current_floor != g and current_floor <= f:
        # Calculate the next floor based on the up and down buttons
        next_floor = min(current_floor + u, g)
        next_floor = max(current_floor - d, 1)

        # Update the current floor and pushes
        current_floor = next_floor
        pushes += 1

    # Check if we reached the goal floor
    if current_floor == g:
        return pushes
    else:
        return "use the stairs"

