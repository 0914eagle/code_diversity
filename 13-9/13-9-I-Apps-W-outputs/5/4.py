
def get_min_light_radius(lanterns, street_length):
    # Sort the lanterns by their position
    lanterns.sort()
    
    # Initialize the minimum light radius to the maximum possible value
    min_radius = float('inf')
    
    # Iterate over each pair of adjacent lanterns
    for i in range(len(lanterns) - 1):
        # Calculate the distance between the two lanterns
        distance = lanterns[i + 1] - lanterns[i]
        
        # If the distance is less than the minimum light radius, update the minimum light radius
        if distance < min_radius:
            min_radius = distance
    
    # Return the minimum light radius
    return min_radius

