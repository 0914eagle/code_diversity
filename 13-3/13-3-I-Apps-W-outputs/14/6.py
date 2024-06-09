
def solve(n, B):
    # Initialize an empty list to store the chosen points
    chosen_points = []

    # Iterate through the given points
    for i in range(n):
        # If the current point is not in the chosen points list, add it
        if B[i] not in chosen_points:
            chosen_points.append(B[i])

    # Return the chosen points in the required format
    return " ".join(map(str, chosen_points))

