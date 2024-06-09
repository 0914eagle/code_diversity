
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors needed
        l, r, x = conditions[i]

        # Get the number of squares in the current range
        num_squares = r - l + 1

        # Calculate the number of ways to paint the current range with x different colors
        num_ways_range = x ** num_squares

        # Multiply the number of ways to paint the current range by the number of ways to paint the previous ranges
        num_ways *= num_ways_range

        # Modulo the result to avoid overflow
        num_ways %= 1000000007

    # Return the number of ways to paint the squares
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

