
def solve(n, lengths, terrain, stamina):
    # Initialize variables
    time = 0
    position = 0
    current_terrain = terrain[0]
    current_stamina = stamina

    # Iterate through the segments
    for i in range(n):
        # Check if Bob can move to the next segment
        if current_terrain == "W" and current_stamina >= 1:
            # Bob can walk, so reduce stamina and move forward
            current_stamina -= 1
            position += 1
        elif current_terrain == "L" and current_stamina >= 2:
            # Bob can fly, so reduce stamina and move forward
            current_stamina -= 2
            position += 1
        elif current_terrain == "G" and current_stamina >= 3:
            # Bob can swim, so reduce stamina and move forward
            current_stamina -= 3
            position += 1
        else:
            # Bob cannot move, so break the loop
            break

        # Update the current terrain and stamina
        current_terrain = terrain[i % n]
        current_stamina = max(current_stamina, 0)

        # Add time based on the current terrain
        if current_terrain == "W":
            time += 5
        elif current_terrain == "L":
            time += 1
        elif current_terrain == "G":
            time += 3

    # Return the minimum time needed to reach Alice's nest
    return time

