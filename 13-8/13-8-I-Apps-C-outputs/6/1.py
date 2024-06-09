
def solve(n, positions):
    # Sort the positions of the swimmers by their x-coordinate
    positions.sort(key=lambda x: x[0])

    # Initialize the x-coordinate of the first lifeguard
    x1 = positions[0][0]

    # Initialize the x-coordinate of the second lifeguard
    x2 = positions[-1][0]

    # Initialize the number of swimmers assigned to each lifeguard
    num_swimmers1 = 0
    num_swimmers2 = 0

    # Loop through the positions of the swimmers
    for i in range(n):
        # Calculate the distance between the current swimmer and the first lifeguard
        dist1 = abs(positions[i][0] - x1) + abs(positions[i][1] - x1)

        # Calculate the distance between the current swimmer and the second lifeguard
        dist2 = abs(positions[i][0] - x2) + abs(positions[i][1] - x2)

        # Assign the current swimmer to the lifeguard with the shorter distance
        if dist1 < dist2:
            num_swimmers1 += 1
        else:
            num_swimmers2 += 1

    # Print the x-coordinates of the two lifeguards
    print(x1, x2)

    # Return the number of swimmers assigned to each lifeguard
    return num_swimmers1, num_swimmers2

