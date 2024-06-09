
def get_lifeguard_positions(n, swimmers):
    # Sort the swimmers by their x-coordinate
    swimmers.sort(key=lambda x: x[0])

    # Initialize the positions of the lifeguards
    lifeguard1_x = 0
    lifeguard2_x = 0

    # Loop through the swimmers and assign them to a lifeguard
    for i in range(n):
        # Calculate the distance between the current swimmer and the lifeguards
        dist1 = abs(swimmers[i][0] - lifeguard1_x)
        dist2 = abs(swimmers[i][0] - lifeguard2_x)

        # Assign the swimmer to the lifeguard with the shorter distance
        if dist1 < dist2:
            lifeguard1_x += swimmers[i][0]
        else:
            lifeguard2_x += swimmers[i][0]

    # Return the positions of the lifeguards
    return [lifeguard1_x, lifeguard2_x]

