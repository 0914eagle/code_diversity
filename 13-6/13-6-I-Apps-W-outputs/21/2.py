
def solve(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    segment = 0
    terrain_type = terrain[segment]
    movement = "walk"

    # Loop through each segment
    while segment < n:
        # Check if Bob can move
        if stamina > 0:
            # Check if Bob can fly
            if terrain_type == "L" and movement != "fly":
                movement = "fly"
                stamina -= 1
            # Check if Bob can swim
            elif terrain_type == "W" and movement != "swim":
                movement = "swim"
                stamina -= 1
            # Check if Bob can walk
            elif terrain_type == "G" and movement != "walk":
                movement = "walk"
                stamina += 1

        # Move Bob
        if movement == "fly":
            time += 1
            stamina -= 1
        elif movement == "swim":
            time += 3
            stamina -= 1
        elif movement == "walk":
            time += 5
            stamina += 1

        # Update variables
        segment += 1
        if segment < n:
            terrain_type = terrain[segment]

    # Return result
    return time

