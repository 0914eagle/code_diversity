
def get_min_heaters(n, r, house):
    # Initialize the number of heaters as 0
    num_heaters = 0
    
    # Sort the house positions
    sorted_positions = sorted(house)
    
    # Iterate through the sorted positions
    for i in range(len(sorted_positions)):
        # Check if the current position is within the range of the current heater
        if sorted_positions[i] <= r:
            # If the current position is within the range, increase the number of heaters
            num_heaters += 1
        else:
            # If the current position is not within the range, break the loop
            break
    
    # Return the number of heaters
    return num_heaters

