
def find_lipschitz_constant(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the Lipschitz constant to the maximum possible value
    lipschitz_constant = float('inf')

    # Iterate over the points and calculate the Lipschitz constant
    for i in range(len(sorted_points) - 1):
        x1, y1 = sorted_points[i]
        x2, y2 = sorted_points[i + 1]
        lipschitz_constant = min(lipschitz_constant, abs(y1 - y2) / abs(x1 - x2))

    return lipschitz_constant

