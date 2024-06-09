
import math

def solve(n, portals):
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the current room to 1
    current_room = 1
    # Initialize the number of crosses on the ceiling to 1
    crosses = 1

    # Loop through each room
    for i in range(n):
        # If the number of crosses on the ceiling is odd
        if crosses % 2 == 1:
            # Use the second portal (it leads to room p_i)
            current_room = portals[i]
        else:
            # Use the first portal (it leads to room i + 1)
            current_room += 1

        # Increment the number of moves
        moves += 1
        # Increment the number of crosses on the ceiling
        crosses += 1

    # Return the number of moves modulo 1000000007
    return moves % 1000000007

