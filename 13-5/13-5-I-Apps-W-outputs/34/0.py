
def get_shortest_time(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    segment = 0
    terrain_type = terrain[segment]
    length = lengths[segment]

    # Loop through each segment
    while segment < n:
        # Check terrain type
        if terrain_type == "G":
            # Walking is relaxing, gain stamina
            stamina += length
        elif terrain_type == "W":
            # Swimming is relaxing, gain stamina
            stamina += length
        else:
            # Flying is tiring, spend stamina
            stamina -= length

        # Check if stamina is negative
        if stamina < 0:
            # Not enough stamina, cannot continue
            return -1

        # Add time based on terrain type
        if terrain_type == "G":
            time += length * 5
        elif terrain_type == "W":
            time += length * 3
        else:
            time += length * 1

        # Increment segment and terrain type
        segment += 1
        if segment < n:
            terrain_type = terrain[segment]
            length = lengths[segment]

    # Return shortest time
    return time

