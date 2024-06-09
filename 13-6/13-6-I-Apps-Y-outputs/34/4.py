
def get_button_pushes(f, s, g, u, d):
    # Initialize variables
    pushes = 0
    current_floor = s

    # Loop until we reach the goal floor or exceed the number of floors
    while current_floor != g and current_floor <= f:
        # Calculate the next floor based on the UP and DOWN buttons
        next_floor = current_floor + u if current_floor + u <= f else current_floor - d if current_floor - d >= 1 else None

        # If the next floor is None, return "use the stairs"
        if next_floor is None:
            return "use the stairs"

        # Increment the pushes and set the current floor to the next floor
        pushes += 1
        current_floor = next_floor

    # Return the number of pushes
    return pushes

