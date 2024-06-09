
def antimatter_rain(droplets, sensors):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over the droplets
    for droplet in droplets:
        # Initialize a variable to store the minimum y-coordinate that the droplet can disintegrate
        min_y = float('inf')
        
        # Iterate over the sensors
        for sensor in sensors:
            # Check if the droplet intersects with the sensor
            if droplet[0] >= sensor[0] and droplet[0] <= sensor[1] and droplet[1] >= sensor[2]:
                # Update the minimum y-coordinate if necessary
                min_y = min(min_y, sensor[2])
        
        # Add the minimum y-coordinate to the results list
        results.append(min_y)
    
    # Return the results list
    return results

