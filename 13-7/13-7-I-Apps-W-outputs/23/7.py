
def solve(n, paths):
    # Initialize a set to store the colors
    colors = set()
    # Iterate over the paths
    for path in paths:
        # If the two squares in the path have the same color, add the color to the set
        if path[0] != path[1]:
            colors.add(path[0])
            colors.add(path[1])
    # Return the length of the set (i.e., the number of colors needed)
    return len(colors)

