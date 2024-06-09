
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors required
        l, r, x = conditions[i]

        # Calculate the number of ways to paint the squares with the current condition
        num_ways *= count_ways(N, l, r, x)

        # Reduce the number of ways to paint the squares modulo 10^9+7
        num_ways %= 1000000007

    return num_ways

def count_ways(N, l, r, x):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each square from left to right
    for i in range(l, r+1):
        # If the current square is not painted, add the number of ways to paint it
        if i not in painted_squares:
            num_ways *= x

            # Reduce the number of ways to paint the squares modulo 10^9+7
            num_ways %= 1000000007

    return num_ways

if __name__ == '__main__':
    # Read the input from stdin
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))

    # Call the paint_squares function and print the result
    print(paint_squares(N, M, conditions))

