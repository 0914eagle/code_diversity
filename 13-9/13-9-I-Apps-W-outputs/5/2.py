
def get_min_light_radius(lanterns, street_length):
    # Sort the lanterns by their position
    lanterns.sort()
    
    # Initialize the minimum light radius as the distance between the first two lanterns
    min_light_radius = lanterns[1] - lanterns[0]
    
    # Iterate over the lanterns
    for i in range(1, len(lanterns)):
        # Calculate the distance between the current lantern and the previous lantern
        distance = lanterns[i] - lanterns[i-1]
        
        # Update the minimum light radius if necessary
        if distance > min_light_radius:
            min_light_radius = distance
    
    # Return the minimum light radius
    return min_light_radius

