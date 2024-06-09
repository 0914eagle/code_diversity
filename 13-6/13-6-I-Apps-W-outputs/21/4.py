
def solve(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    current_terrain = "G"
    current_length = 0
    
    # Iterate through the segments
    for i in range(n):
        # Check the terrain type
        if terrain[i] == "W":
            # Swimming is only possible on water
            if current_terrain == "W":
                # Swim for the length of the segment
                time += 3 * lengths[i]
                stamina += lengths[i]
                current_length += lengths[i]
            else:
                # Fly over the water segment
                time += 1 * lengths[i]
                stamina -= lengths[i]
                current_length += lengths[i]
        elif terrain[i] == "L":
            # Flying is only possible over lava
            if current_terrain == "L":
                # Fly for the length of the segment
                time += 1 * lengths[i]
                stamina -= lengths[i]
                current_length += lengths[i]
            else:
                # Swim over the lava segment
                time += 3 * lengths[i]
                stamina += lengths[i]
                current_length += lengths[i]
        else:
            # Walking is possible on grass and water
            time += 5 * lengths[i]
            stamina += lengths[i]
            current_length += lengths[i]
        
        # Update the current terrain type
        current_terrain = terrain[i]
    
    # Return the minimum time needed to reach Alice's nest
    return time

