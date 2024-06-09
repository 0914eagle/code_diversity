
def find_lipschitz_constant(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the Lipschitz constant to zero
    lipschitz_constant = 0

    # Iterate over the points
    for i in range(len(sorted_points) - 1):
        # Calculate the difference between the current and next point
        diff = sorted_points[i + 1][1] - sorted_points[i][1]

        # Update the Lipschitz constant if the difference is larger than the current value
        lipschitz_constant = max(lipschitz_constant, abs(diff))

    return lipschitz_constant

