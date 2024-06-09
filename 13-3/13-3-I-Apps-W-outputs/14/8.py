
def solve(n, B):
    # Initialize a list to store the chosen points
    chosen_points = []

    # Iterate through the edges of the polygon
    for i in range(n):
        # If the current edge is not chosen by the court, choose the next point
        if i not in B:
            chosen_points.append(i)

    # Return the chosen points in the required format
    return " ".join(str(point) for point in chosen_points)

