
def get_min_distance(locations, capacity):
    # Sort the locations in ascending order
    locations.sort(key=lambda x: x[0])
    
    # Initialize the variables
    current_location = 0
    current_capacity = 0
    total_distance = 0
    
    # Loop through each location
    for location in locations:
        # Check if the current location is the post office
        if location[0] == 0:
            continue
        
        # Check if the current location is within the capacity
        if current_capacity + location[1] <= capacity:
            # Add the letters to the current capacity
            current_capacity += location[1]
        else:
            # Calculate the distance to the current location
            distance = abs(current_location - location[0])
            
            # Add the distance to the total distance
            total_distance += distance
            
            # Set the current location to the current location
            current_location = location[0]
            
            # Set the current capacity to the number of letters
            current_capacity = location[1]
    
    # Return the total distance
    return total_distance

