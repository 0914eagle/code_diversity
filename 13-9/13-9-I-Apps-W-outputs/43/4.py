
def solve_cube(k):
    # Initialize the cube with all white colors
    cube = [[("w", "w", "w")] * k for _ in range(k)]

    # Loop through each layer of the cube
    for i in range(k):
        # Loop through each row of the layer
        for j in range(k):
            # Loop through each element of the row
            for elem in cube[i][j]:
                # If the element is white, check if it has exactly 2 white neighbors
                if elem == "w" and not (count_neighbors(cube, i, j, elem) == 2):
                    # If it doesn't have 2 white neighbors, return -1
                    return -1
                # If the element is black, check if it has exactly 2 black neighbors
                if elem == "b" and not (count_neighbors(cube, i, j, elem) == 2):
                    # If it doesn't have 2 black neighbors, return -1
                    return -1

    # If all the conditions are satisfied, return the cube
    return cube

def count_neighbors(cube, i, j, elem):
    # Initialize the count of neighbors to 0
    count = 0
    # Check if the element has a neighbor in the top row
    if i > 0 and cube[i-1][j][j] == elem:
        count += 1
    # Check if the element has a neighbor in the bottom row
    if i < len(cube) - 1 and cube[i+1][j][j] == elem:
        count += 1
    # Check if the element has a neighbor in the left column
    if j > 0 and cube[i][j-1][j] == elem:
        count += 1
    # Check if the element has a neighbor in the right column
    if j < len(cube) - 1 and cube[i][j+1][j] == elem:
        count += 1
    # Return the count of neighbors
    return count

cube = solve_cube(int(input()))
if cube == -1:
    print(-1)
else:
    for layer in cube:
        for row in layer:
            print("".join(row))
        print()

