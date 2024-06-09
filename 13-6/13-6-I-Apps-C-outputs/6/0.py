
def antimatter_rain(droplets, sensors):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over the droplets
    for droplet in droplets:
        # Initialize a variable to store the y-coordinate of the sensor that the droplet will disintegrate with
        sensor_y = 0
        
        # Iterate over the sensors
        for sensor in sensors:
            # Check if the droplet is within the range of the sensor
            if droplet[0] >= sensor[0] and droplet[0] <= sensor[1]:
                # Check if the droplet is at a higher y-coordinate than the sensor
                if droplet[1] > sensor[2]:
                    # Update the y-coordinate of the sensor that the droplet will disintegrate with
                    sensor_y = sensor[2]
                    break
        
        # Add the y-coordinate of the sensor that the droplet will disintegrate with to the results list
        results.append(sensor_y)
    
    return results

