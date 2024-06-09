
def count_valid_colorings(n, a):
    # Initialize a 2D array to store the number of colored edges for each hexagon
    colored_edges = [[0] * n for _ in range(n)]

    # Loop through each row of the input array
    for i in range(n):
        # Loop through each element in the row
        for j in range(n):
            # If the element is not -1, add the number of colored edges for the hexagon to the total
            if a[i][j] != -1:
                colored_edges[i][j] += a[i][j]

    # Initialize a set to store the valid colorings
    valid_colorings = set()

    # Loop through each row of the input array
    for i in range(n):
        # Loop through each element in the row
        for j in range(n):
            # If the element is not -1, add the number of colored edges for the hexagon to the total
            if a[i][j] != -1:
                valid_colorings.add(tuple(colored_edges[i][j]))

    # Return the number of valid colorings
    return len(valid_colorings)

