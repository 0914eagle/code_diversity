
def solve(n, paths):
    # Initialize a set to store the colors
    colors = set()
    # Loop through each path
    for path in paths:
        # Add the colors of the squares in the path to the set
        colors.update(path)
    # Return the length of the set, which is the minimum number of colors needed
    return len(colors)

