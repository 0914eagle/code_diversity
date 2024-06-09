
def solve(n, p, m, names, points):
    # Initialize a dictionary to store the names and points
    name_points = {}

    # Iterate over the input names and points
    for i in range(n):
        # Add the name and point to the dictionary
        name_points[names[i]] = points[i]

    # Find the winners
    winners = [name for name, point in name_points.items() if point >= p]

    # Check if there are any winners
    if len(winners) == 0:
        return "No winner!"

    # Return the winners in order
    return "\n".join([f"{name} wins!" for name in winners])

