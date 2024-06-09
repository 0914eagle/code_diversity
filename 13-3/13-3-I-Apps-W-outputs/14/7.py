
def max_area(n, B):
    # Initialize an empty list to store the chosen points
    chosen_points = []

    # Iterate through the given points
    for i in range(n):
        # If the current point is not already in the list, add it
        if B[i] not in chosen_points:
            chosen_points.append(B[i])

    # Return the chosen points in the desired order
    return chosen_points

