
def antimatter_rain(droplets, sensors):
    # Initialize an empty list to store the results
    results = []

    # Loop through each droplet
    for droplet in droplets:
        # Initialize a variable to store the disintegration point
        disintegration_point = 0

        # Loop through each sensor
        for sensor in sensors:
            # Check if the droplet intersects with the sensor
            if droplet[0] <= sensor[1] and droplet[1] >= sensor[0]:
                # If it intersects, set the disintegration point to the sensor's y-coordinate
                disintegration_point = sensor[2]
                break

        # Add the disintegration point to the results list
        results.append(disintegration_point)

    return results

