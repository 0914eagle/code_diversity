
import sys

def knight_moves(x, y):
    # Initialize the number of ways to be 0
    ways = 0

    # Base case: if the knight is already at the destination, return 1
    if x == 0 and y == 0:
        return 1

    # Recursive case: try moving the knight to the two possible squares
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            # Check if the square is valid and not the current position
            if i >= 0 and j >= 0 and (i, j) != (x, y):
                ways += knight_moves(i, j)

    # Return the number of ways modulo 10^9 + 7
    return ways % 1000000007

if __name__ == "__main__":
    x, y = map(int, sys.stdin.readline().split())
    print(knight_moves(x, y))

