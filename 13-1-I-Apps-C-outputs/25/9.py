
def get_minimum_moves(n, positions):
    # Sort the positions of the cars
    positions.sort()
    # Initialize the minimum number of moves to 0
    min_moves = 0
    # Loop through the positions of the cars
    for i in range(n):
        # If the position of the current car is not equal to its index, we need to move the car
        if positions[i] != i + 1:
            # Increment the minimum number of moves
            min_moves += 1
    # Return the minimum number of moves
    return min_moves

