
def solve(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    segment = 0
    direction = 1

    # Loop through each segment
    while segment < n:
        # Check terrain type
        if terrain[segment] == "G":
            # Grass, walk or fly
            if stamina > 0:
                # Fly
                stamina -= 1
                time += 1
            else:
                # Walk
                stamina += 1
                time += 5
        elif terrain[segment] == "W":
            # Water, swim or fly
            if stamina > 0:
                # Fly
                stamina -= 1
                time += 1
            else:
                # Swim
                stamina += 1
                time += 3
        else:
            # Lava, cannot fly
            if stamina > 1:
                # Walk or swim
                stamina -= 2
                time += 5
            else:
                # Cannot fly or walk/swim, so switch direction
                direction *= -1
                time += 1

        # Update segment and stamina
        segment += direction
        stamina = max(stamina, 0)

    # Return total time
    return time

