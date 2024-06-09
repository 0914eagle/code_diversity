
def solve(n, p, m, names, points):
    # Initialize a dictionary to store the names and points
    name_points = {}

    # Iterate over the input names and points
    for i in range(m):
        # Extract the name and points from the input
        name, points = names[i], points[i]

        # If the name is not in the dictionary, add it and set its points to the current points
        if name not in name_points:
            name_points[name] = points
        # Otherwise, add the current points to the total points of the name
        else:
            name_points[name] += points

    # Initialize a list to store the winners
    winners = []

    # Iterate over the names and points
    for name, points in name_points.items():
        # If the points are greater than or equal to the minimum required score, add the name to the winners list
        if points >= p:
            winners.append(name)

    # If no one reached the minimum required score, return "No winner!"
    if not winners:
        return "No winner!"

    # Otherwise, return the winners in the order they reached the minimum required score
    return "\n".join([f"{winner} wins!" for winner in winners])

