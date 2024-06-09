
def solve(n, swimmers):
    # Sort the swimmers by their x coordinate
    swimmers.sort(key=lambda x: x[0])

    # Initialize the positions of the lifeguards
    lifeguard1_x = 0
    lifeguard2_x = 0

    # Loop through the swimmers and assign them to a lifeguard
    for i in range(n):
        # If the current swimmer is closer to lifeguard 1, assign them to lifeguard 1
        if abs(swimmers[i][0] - lifeguard1_x) <= abs(swimmers[i][0] - lifeguard2_x):
            lifeguard1_x += 1
        # Otherwise, assign them to lifeguard 2
        else:
            lifeguard2_x += 1

    # Return the positions of the lifeguards
    return [lifeguard1_x, lifeguard2_x]

