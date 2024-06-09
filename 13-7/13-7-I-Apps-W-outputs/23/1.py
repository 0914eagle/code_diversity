
def solve(n, paths):
    # Initialize a set to store the colors
    colors = set()
    # Loop through each path and add the colors of the two squares to the set
    for path in paths:
        colors.add(path[0])
        colors.add(path[1])
    # Return the length of the set, which is the minimum number of colors needed
    return len(colors)

