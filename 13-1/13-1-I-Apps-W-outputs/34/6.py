
import sys

def knight_moves(x, y):
    # Initialize the number of ways to reach (x, y) as 0
    ways = 0

    # Base case: if we are already at (x, y), there is only 1 way to reach there
    if x == y:
        return 1

    # Recursive case: consider all possible moves for the knight
    for i in range(x):
        for j in range(y):
            # If the knight can move to (i, j), add the number of ways to reach (i, j) to the total number of ways
            if (i + 1, j + 2) == (x, y) or (i + 2, j + 1) == (x, y):
                ways += knight_moves(i, j)

    # Return the total number of ways modulo 10^9 + 7
    return ways % 1000000007

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(knight_moves(x, y))

