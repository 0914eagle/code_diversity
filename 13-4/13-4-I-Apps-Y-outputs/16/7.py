
def solve(N, M, coordinates):
    # Sort the coordinates in ascending order
    sorted_coordinates = sorted(coordinates)

    # Initialize the minimum number of moves to achieve the objective as infinity
    min_moves = float('inf')

    # Loop through all possible starting positions for the pieces
    for i in range(N):
        # Initialize the current position of the pieces as the ith coordinate
        current_position = sorted_coordinates[i]

        # Initialize the number of moves made so far as 0
        moves_made = 0

        # Loop through all the coordinates to visit
        for j in range(M):
            # Calculate the distance between the current position and the next coordinate to visit
            distance = abs(sorted_coordinates[j] - current_position)

            # If the distance is 0, it means we are already at the coordinate, so we don't need to move
            if distance == 0:
                continue

            # If the distance is 1, we can move to the next coordinate in 1 move
            elif distance == 1:
                moves_made += 1
                current_position = sorted_coordinates[j]

            # If the distance is greater than 1, we need to move the piece back and forth to cover the distance
            else:
                moves_made += 2
                current_position = sorted_coordinates[j]

        # If the minimum number of moves required to achieve the objective has not been found yet,
        # or if the current number of moves made is less than the minimum number of moves required,
        # update the minimum number of moves required
        if min_moves == float('inf') or moves_made < min_moves:
            min_moves = moves_made

    return min_moves

