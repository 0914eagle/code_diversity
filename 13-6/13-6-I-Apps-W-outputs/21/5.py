
def solve(n, lengths, terrain, stamina):
    # Initialize variables
    time = 0
    position = 0
    current_terrain = terrain[0]
    current_stamina = 0

    # Loop through each segment
    for i in range(n):
        # Check if Bob can move to the next segment
        if current_stamina == 0 and current_terrain == "L":
            return -1

        # Calculate the time to move to the next segment
        if current_terrain == "G":
            time += 5 * lengths[i]
            current_stamina += lengths[i]
        elif current_terrain == "W":
            time += 3 * lengths[i]
            current_stamina += lengths[i]
        else:
            time += 1 * lengths[i]
            current_stamina -= lengths[i]

        # Update the position and terrain
        position += lengths[i]
        current_terrain = terrain[i % n]

    # Return the time it took Bob to reach Alice's nest
    return time

