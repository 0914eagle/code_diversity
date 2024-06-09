
import sys

def knight_moves(x, y):
    # Initialize the number of ways to reach (x, y) as 0
    ways = 0

    # Base case: if we are already at (x, y), there is only 1 way to get there
    if x == y:
        return 1

    # Recursive case: consider all possible moves for the knight
    for i in range(x):
        for j in range(y):
            # If the knight can move to (i, j), add the number of ways to reach (i, j) to the total number of ways
            if i + 1 == x and j + 2 == y or i + 2 == x and j + 1 == y:
                ways += knight_moves(i, j)

    # Return the total number of ways modulo 10^9 + 7
    return ways % 1000000007

# Read the input from stdin
x, y = map(int, input().split())

# Call the knight_moves function and print the result
print(knight_moves(x, y))

