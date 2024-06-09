
def solve(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    current_terrain = 0
    current_length = 0

    # Loop through the segments
    for i in range(n):
        # Check the terrain type
        if terrain[i] == "G":
            # Grass, Bob can walk
            current_terrain = 1
        elif terrain[i] == "W":
            # Water, Bob can swim
            current_terrain = 2
        else:
            # Lava, Bob can fly
            current_terrain = 3

        # Check if Bob needs to spend stamina
        if current_terrain != current_length:
            # Bob needs to spend stamina
            if current_terrain == 1:
                # Walking, Bob gains 1 stamina
                stamina += 1
            elif current_terrain == 2:
                # Swimming, Bob spends 1 stamina
                stamina -= 1
            elif current_terrain == 3:
                # Flying, Bob spends 1 stamina
                stamina -= 1

        # Check if Bob's stamina is negative
        if stamina < 0:
            # Bob's stamina is negative, he can't continue
            return -1

        # Add the length of the current segment to the total time
        time += lengths[i]

        # Update the current length and terrain
        current_length = current_terrain

    # Return the total time
    return time

