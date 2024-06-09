
def max_area(n, points):
    # Initialize an empty list to store the chosen points
    chosen_points = []
    # Loop through the points and choose the point that is not adjacent to any of the chosen points
    for i in range(n):
        if i not in chosen_points and i-1 not in chosen_points and i+1 not in chosen_points:
            chosen_points.append(i)
    # Return the chosen points in the desired format
    return " ".join(str(point) for point in chosen_points)

