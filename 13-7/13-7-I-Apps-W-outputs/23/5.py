
def solve(n, edges):
    # Initialize a set to store the colors
    colors = set()
    # Loop through each edge and find the minimum number of colors needed
    for edge in edges:
        # If the colors of the two squares are not already in the set, add them
        if edge[0] not in colors:
            colors.add(edge[0])
        if edge[1] not in colors:
            colors.add(edge[1])
    # Return the length of the set (i.e., the minimum number of colors needed)
    return len(colors)

