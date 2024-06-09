
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for i in range(M):
        # Get the range of squares and the number of different colors
        l, r, x = conditions[i]
        num_colors = x

        # Calculate the number of ways to paint the squares in the current range
        num_ways_range = (N - r + 1) * (N - l + 1)

        # Calculate the number of ways to paint the squares with the current number of colors
        num_ways_colors = num_colors ** (r - l + 1)

        # Update the number of ways to paint the squares
        num_ways *= num_ways_range // num_ways_colors

    # Return the number of ways to paint the squares modulo 10^9+7
    return num_ways % 1000000007

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(paint_squares(N, M, conditions))

