
def antimatter_rain(droplets, sensors):
    # Initialize a dictionary to store the y-coordinates of the disintegrating droplets
    disintegrating_droplets = {}

    # Iterate over the droplets
    for droplet in droplets:
        # Initialize a variable to store the y-coordinate of the disintegrating droplet
        disintegrating_y = 0

        # Iterate over the sensors
        for sensor in sensors:
            # Check if the droplet intersects with the sensor
            if droplet[0] <= sensor[1] and sensor[0] <= droplet[1]:
                # Update the y-coordinate of the disintegrating droplet
                disintegrating_y = sensor[2]
                break

        # Add the y-coordinate of the disintegrating droplet to the dictionary
        disintegrating_droplets[droplet[0]] = disintegrating_y

    return disintegrating_droplets

