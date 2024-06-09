
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
            if droplet[0] >= sensor[0] and droplet[0] <= sensor[1] and droplet[1] == sensor[2]:
                # If the droplet intersects with the sensor, set the disintegration point to the sensor's y-coordinate
                disintegration_point = sensor[2]
                break

        # Add the disintegration point for the current droplet to the dictionary
        disintegration_points[droplet] = disintegration_point

    return disintegration_points

def f2(disintegration_points):
    # Initialize a list to store the output
    output = []

    # Iterate over the disintegration points
    for droplet, point in disintegration_points.items():
        # Add the disintegration point for the current droplet to the output list
        output.append(point)

    return output

if __name__ == '__main__':
    # Read the input
    d, s = map(int, input().split())
    droplets = [tuple(map(int, input().split())) for _ in range(d)]
    sensors = [tuple(map(int, input().split())) for _ in range(s)]

    # Call the first function to get the disintegration points
    disintegration_points = f1(droplets, sensors)

    # Call the second function to get the output
    output = f2(disintegration_points)

    # Print the output
    for point in output:
        print(point)

