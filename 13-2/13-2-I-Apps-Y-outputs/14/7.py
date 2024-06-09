
def solve(n, p, m, names, points):
    # Initialize a dictionary to store the names and points
    name_points = {}

    # Iterate through the list of names and points
    for i in range(len(names)):
        # Check if the current name is already in the dictionary
        if names[i] not in name_points:
            # If not, add it to the dictionary with the current points
            name_points[names[i]] = points[i]
        else:
            # If the name is already in the dictionary, add the current points to the total points
            name_points[names[i]] += points[i]

    # Initialize a list to store the winners
    winners = []

    # Iterate through the dictionary and check if the points are greater than or equal to the minimum required score
    for name, points in name_points.items():
        if points >= p:
            # If so, add the name to the list of winners
            winners.append(name)

    # If no one reached the minimum required score, return "No winner!"
    if not winners:
        return "No winner!"

    # Otherwise, return the names of the winners, separated by newlines
    return "\n".join(winners) + " wins!"

