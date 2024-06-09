
def solve(f, s, g, u, d):
    # Initialize variables
    pushes = 0
    current_floor = s

    # Loop until we reach the goal floor or exceed the number of floors
    while current_floor != g and current_floor <= f:
        # Calculate the next floor based on the up and down buttons
        next_floor = current_floor + u if current_floor + u <= f else current_floor - d if current_floor - d >= 1 else None

        # If the next floor is None, we cannot reach the goal floor
        if next_floor is None:
            return "use the stairs"

        # Update the current floor and the number of pushes
        current_floor = next_floor
        pushes += 1

    # Return the number of pushes
    return pushes

