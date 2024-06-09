
def solve(n, lengths, terrain):
    # Initialize variables
    stamina = 0
    time = 0
    segment = 0
    total_time = 0
    
    # Loop through each segment
    while segment < n:
        # Check terrain type
        if terrain[segment] == "G":
            # Walk on grass
            stamina += 1
            time += 5
        elif terrain[segment] == "W":
            # Swim in water
            stamina += 1
            time += 3
        else:
            # Fly over lava
            stamina -= 1
            time += 1
        
        # Add segment length to total time
        total_time += time
        
        # Increase segment index
        segment += 1
    
    # Return minimum time to reach Alice's nest
    return total_time

