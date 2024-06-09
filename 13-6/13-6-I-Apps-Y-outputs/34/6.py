
def solve(f, s, g, u, d):
    # Initialize variables
    pushes = 0
    current_floor = s

    # Loop until we reach the goal floor or exceed the number of floors
    while current_floor != g and current_floor <= f:
        # Calculate the next floor based on the up and down buttons
        next_floor = current_floor + u if current_floor + u <= f else current_floor
        next_floor = current_floor - d if current_floor - d >= 1 else current_floor

        # Increment the number of pushes and update the current floor
        pushes += 1
        current_floor = next_floor

    # If we reached the goal floor, return the number of pushes
    if current_floor == g:
        return pushes
    # If we exceeded the number of floors, return "use the stairs"
    else:
        return "use the stairs"

