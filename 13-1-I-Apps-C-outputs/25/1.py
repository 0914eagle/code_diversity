
def sort_railway_cars(n, positions):
    # Sort the positions of the cars
    positions.sort()
    # Initialize the number of moves to 0
    moves = 0
    # Loop through the positions of the cars
    for i in range(n):
        # If the position of the current car is not equal to its index, we need to move the car
        if positions[i] != i + 1:
            # Increment the number of moves
            moves += 1
    # Return the number of moves
    return moves

