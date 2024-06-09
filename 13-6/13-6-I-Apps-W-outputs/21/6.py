
def solve(n, lengths, terrain, stamina):
    # Initialize variables
    time = 0
    position = 0
    current_terrain = terrain[0]
    current_stamina = stamina

    # Loop through each segment
    for i in range(n):
        # Calculate the time it takes to travel the current segment
        if current_terrain == "G":
            time += 5 * lengths[i]
        elif current_terrain == "W":
            time += 3 * lengths[i]
        else:
            time += 1 * lengths[i]

        # Update the position and stamina
        position += lengths[i]
        current_stamina -= lengths[i]

        # Check if Bob needs to switch terrain
        if current_terrain == "G" and position % 2 == 0:
            current_terrain = "W"
        elif current_terrain == "W" and position % 2 == 1:
            current_terrain = "G"

        # Check if Bob needs to fly
        if current_terrain == "L" and current_stamina < 0:
            time += abs(current_stamina)
            current_stamina = 0

        # Update the current stamina
        if current_terrain == "G" or current_terrain == "W":
            current_stamina += lengths[i]
        else:
            current_stamina -= lengths[i]

    return time

