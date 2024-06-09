
def solve(n, lengths, terrain):
    # Initialize variables
    stamina = 0
    time = 0
    segment = 0
    is_flying = False
    
    # Loop through each segment
    for i in range(n):
        # Get the length and terrain type of the current segment
        length = lengths[i]
        terrain_type = terrain[i]
        
        # Check if Bob can fly over the current segment
        if terrain_type == "W" and stamina >= length:
            # Fly over the segment and spend stamina
            stamina -= length
            time += length
            is_flying = True
        else:
            # Walk or swim over the segment
            if terrain_type == "G":
                # Walk over the segment and gain stamina
                stamina += 1
                time += 5
            else:
                # Swim over the segment and gain stamina
                stamina += 1
                time += 3
        
        # Check if Bob has reached the last segment
        if i == n - 1:
            # If Bob is flying, he can reach Alice's nest immediately
            if is_flying:
                time += length
            # If Bob is walking or swimming, he needs to spend stamina to reach Alice's nest
            else:
                # Calculate the time it takes to reach Alice's nest
                time += length * 5
        
    # Return the minimum time it takes for Bob to reach Alice's nest
    return time

