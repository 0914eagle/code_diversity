
def solve(N, M, coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum number of moves to be the number of pieces
    min_moves = N

    # Iterate over all possible starting positions for the first piece
    for i in range(N):
        # Initialize the current position of the first piece as the ith coordinate
        current_position = sorted_coordinates[i]

        # Initialize the number of moves to 0
        moves = 0

        # Iterate over all the remaining coordinates
        for j in range(i+1, N):
            # Calculate the distance between the current position and the next coordinate
            distance = sorted_coordinates[j] - current_position

            # If the distance is 1, move the piece to the next coordinate
            if distance == 1:
                current_position = sorted_coordinates[j]
                moves += 1

            # If the distance is -1, move the piece to the previous coordinate
            elif distance == -1:
                current_position = sorted_coordinates[j-1]
                moves += 1

            # If the distance is greater than 1, we cannot move the piece to the next coordinate, so break the loop
            else:
                break

        # If we have visited all the coordinates, update the minimum number of moves if necessary
        if moves == M:
            min_moves = min(min_moves, moves)

    return min_moves

