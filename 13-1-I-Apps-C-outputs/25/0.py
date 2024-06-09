
def sort_railway_cars(n, positions):
    # Sort the positions of the cars
    positions.sort()
    # Initialize the number of moves to 0
    moves = 0
    # Loop through the positions of the cars
    for i in range(n):
        # If the position of the car is not in its correct position
        if positions[i] != i + 1:
            # Teleport the car to its correct position
            moves += 1
    # Return the number of moves
    return moves

