
def find_positions(n, swimmers):
    # Sort the swimmers by their x coordinates
    swimmers.sort(key=lambda x: x[0])

    # Initialize the positions of the lifeguards
    guard1_x = 0
    guard2_x = 0

    # Loop through the swimmers and assign them to a guard
    for i in range(n):
        # Calculate the distance between the current swimmer and each guard
        dist1 = abs(swimmers[i][0] - guard1_x)
        dist2 = abs(swimmers[i][0] - guard2_x)

        # Assign the swimmer to the guard with the shortest distance
        if dist1 < dist2:
            guard1_x += swimmers[i][0]
        else:
            guard2_x += swimmers[i][0]

    # Return the positions of the lifeguards
    return [guard1_x, guard2_x]

