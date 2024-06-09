
import sys

def knight_moves(x, y):
    # Initialize the number of ways to be 0
    ways = 0

    # Base case: if the knight is already at the destination, return 1
    if x == y == 0:
        return 1

    # Recursive case: try moving the knight to the two possible squares
    for i in range(2):
        for j in range(2):
            # Calculate the new position of the knight
            new_x = x + i
            new_y = y + j

            # If the new position is valid, recurse and add the number of ways to reach the new position
            if 0 <= new_x <= 1000000 and 0 <= new_y <= 1000000:
                ways += knight_moves(new_x, new_y)

    # Return the number of ways modulo 10^9 + 7
    return ways % 1000000007

if __name__ == "__main__":
    x, y = map(int, sys.stdin.readline().split())
    print(knight_moves(x, y))

