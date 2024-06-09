
import sys

def knight_moves(x, y):
    # Initialize the number of ways to be 0
    ways = 0

    # Base case: if the knight is already at the destination, return 1
    if x == 0 and y == 0:
        return 1

    # Recursive case: try moving the knight to the two possible squares
    # and add the number of ways to reach the destination from each square
    ways += knight_moves(x-1, y-2)
    ways += knight_moves(x-2, y-1)

    # Return the number of ways modulo 10^9 + 7
    return ways % 1000000007

if __name__ == "__main__":
    x, y = map(int, sys.stdin.readline().split())
    print(knight_moves(x, y))

