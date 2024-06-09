
def valid_coloring(n, a):
    # Initialize a dictionary to store the number of colored edges for each hexagon
    colored_edges = {}

    # Loop through each row
    for i in range(1, n + 1):
        # If the row index is odd, there are n hexagons in the row
        if i % 2 == 1:
            num_hexagons = n
        # If the row index is even, there are n-1 hexagons in the row
        else:
            num_hexagons = n - 1

        # Loop through each hexagon in the row
        for j in range(1, num_hexagons + 1):
            # If the current hexagon is colored, add the number of colored edges to the dictionary
            if a[i - 1][j - 1] != -1:
                colored_edges[(i, j)] = a[i - 1][j - 1]

    # Initialize a set to store the loops
    loops = set()

    # Loop through each hexagon
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the current hexagon is colored, add the loop to the set of loops
            if (i, j) in colored_edges:
                loops.add(frozenset([(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]))

    # Initialize a set to store the valid colorings
    valid_colorings = set()

    # Loop through each loop
    for loop in loops:
        # If the loop is valid, add it to the set of valid colorings
        if is_valid_loop(loop, colored_edges):
            valid_colorings.add(frozenset(loop))

    return len(valid_colorings)

def is_valid_loop(loop, colored_edges):
    # Initialize a set to store the colored edges in the loop
    loop_edges = set()

    # Loop through each hexagon in the loop
    for hexagon in loop:
        # If the current hexagon is colored, add the colored edge to the set of loop edges
        if hexagon in colored_edges:
            loop_edges.add(colored_edges[hexagon])

    # If the set of loop edges is equal to the set of colored edges in the loop, the loop is valid
    return loop_edges == set(range(1, len(loop_edges) + 1))

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print(valid_coloring(n, a))

