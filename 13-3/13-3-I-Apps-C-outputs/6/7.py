
def f1(droplets, sensors):
    # Initialize a dictionary to store the disintegration points for each droplet
    disintegration_points = {}

    # Iterate over the droplets
    for droplet in droplets:
        # Initialize a variable to store the disintegration point for the current droplet
        disintegration_point = 0

        # Iterate over the sensors
        for sensor in sensors:
            # Check if the current droplet intersects with the current sensor
            if droplet[0] <= sensor[1] and droplet[1] >= sensor[0]:
                # If the droplet intersects with the sensor, update the disintegration point
                disintegration_point = sensor[2]
                break

        # Add the disintegration point for the current droplet to the dictionary
        disintegration_points[droplet] = disintegration_point

    return disintegration_points

def f2(disintegration_points):
    # Initialize a list to store the output
    output = []

    # Iterate over the disintegration points
    for droplet, disintegration_point in disintegration_points.items():
        # Add the disintegration point for the current droplet to the output list
        output.append(disintegration_point)

    return output

if __name__ == '__main__':
    # Read the input
    droplets, sensors = map(int, input().split())
    droplets = [tuple(map(int, input().split())) for _ in range(droplets)]
    sensors = [tuple(map(int, input().split())) for _ in range(sensors)]

    # Call the first function to get the disintegration points
    disintegration_points = f1(droplets, sensors)

    # Call the second function to get the output
    output = f2(disintegration_points)

    # Print the output
    print(*output, sep='\n')

