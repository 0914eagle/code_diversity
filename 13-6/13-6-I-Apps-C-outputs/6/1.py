
def antimatter_rain(droplets, sensors):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each droplet
    for droplet in droplets:
        # Initialize a variable to store the y-coordinate of the sensor that the droplet will disintegrate with
        sensor_y = 0

        # Iterate over each sensor
        for sensor in sensors:
            # Check if the droplet is within the range of the sensor
            if droplet[0] >= sensor[0] and droplet[0] <= sensor[1] and droplet[1] == sensor[2]:
                # If the droplet is within the range of the sensor, set the sensor_y variable to the y-coordinate of the sensor
                sensor_y = sensor[2]
                break

        # Add the y-coordinate of the sensor that the droplet will disintegrate with to the results list
        results.append(sensor_y)

    return results

