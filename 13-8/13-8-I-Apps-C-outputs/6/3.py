
def solve(n, positions):
    # Sort the positions of the swimmers by their x-coordinate
    sorted_positions = sorted(positions, key=lambda x: x[0])

    # Initialize the x-coordinate of the lifeguards
    x1 = 0
    x2 = 0

    # Loop through the sorted positions and assign them to the lifeguards
    for i in range(n):
        if i % 2 == 0:
            x1 += sorted_positions[i][0]
        else:
            x2 += sorted_positions[i][0]

    # Calculate the y-coordinate of the lifeguards by taking the average of the y-coordinates of the swimmers they are responsible for
    y1 = sum([position[1] for position in positions if position[0] <= x1]) / (x1 + 1)
    y2 = sum([position[1] for position in positions if position[0] > x1]) / (n - x1)

    return [x1, y1], [x2, y2]

