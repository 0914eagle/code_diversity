
def get_valid_colorings(n, a):
    # Initialize a 2D array to store the coloring
    coloring = [[0] * n for _ in range(n)]

    # Loop through each row
    for i in range(n):
        # If the row index is odd, there are n hexagons in the row
        if i % 2 == 1:
            num_hexagons = n
        # If the row index is even, there are n-1 hexagons in the row
        else:
            num_hexagons = n - 1

        # Loop through each hexagon in the row
        for j in range(num_hexagons):
            # If the current hexagon is not colored, skip it
            if a[i][j] == -1:
                continue

            # If the current hexagon is colored, check if the coloring is valid
            if not is_valid_coloring(coloring, i, j, a[i][j]):
                return 0

    # If all hexagons are colored and the coloring is valid, return 1
    return 1

def is_valid_coloring(coloring, i, j, color):
    # If the current hexagon is not colored, return True
    if coloring[i][j] == 0:
        return True

    # If the current hexagon is colored, check if the color is equal to the number of colored edges
    if coloring[i][j] != color:
        return False

    # If the current hexagon is colored and the color is equal to the number of colored edges, check if the coloring is valid
    for k in range(len(coloring)):
        # If the current row is the same as the row of the current hexagon, skip it
        if k == i:
            continue

        # If the current row is not the same as the row of the current hexagon, check if the coloring is valid
        if not is_valid_coloring(coloring, k, j, color):
            return False

    # If all rows are valid, return True
    return True

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print(get_valid_colorings(n, a))

