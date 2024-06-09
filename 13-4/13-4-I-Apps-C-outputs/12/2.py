
def max_points(a):
    # Sort the list in descending order
    a.sort(reverse=True)
    # Initialize the maximum points and current points
    max_points, current_points = 0, 0
    # Loop through the list and calculate the points
    for i in range(len(a)):
        current_points += a[i]
        max_points = max(max_points, current_points)
    return max_points

