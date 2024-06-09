
def solve(n, B):
    # Initialize a list to store the chosen points
    chosen_points = []

    # Iterate through the list of chosen points
    for i in range(n):
        # Find the index of the chosen point
        index = B[i]

        # Add the chosen point to the list of chosen points
        chosen_points.append(index)

    # Return the list of chosen points
    return chosen_points

