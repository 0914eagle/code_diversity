
def solve(N, M, coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum number of moves to 0
    min_moves = 0

    # Loop through each coordinate and check if it is visited
    for i in range(M):
        # If the coordinate is not visited, move the piece to that coordinate and increment the minimum number of moves
        if sorted_coordinates[i] != i + 1:
            min_moves += 1

    # Return the minimum number of moves required to visit all coordinates
    return min_moves

