
def solve(n, lengths, terrain):
    # Initialize variables
    time = 0
    stamina = 0
    segment = 0
    distance = 0
    
    # Loop through each segment
    while segment < n:
        # Check terrain type
        if terrain[segment] == "G":
            # Walking on grass, gain stamina
            stamina += 1
            distance += lengths[segment]
        elif terrain[segment] == "W":
            # Swimming on water, gain stamina and move forward
            stamina += 1
            distance += lengths[segment]
        elif terrain[segment] == "L":
            # Flying over lava, spend stamina and move forward
            stamina -= 1
            distance += lengths[segment]
        
        # Update time
        time += lengths[segment]
        
        # Move to next segment
        segment += 1
    
    # Return minimum time
    return time

