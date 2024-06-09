
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for i in range(M):
        # Get the range of squares and the number of different colors required
        l, r, x = conditions[i]

        # Initialize the number of ways to paint the current range
        num_ways_range = 1

        # Loop through each square in the range
        for j in range(l, r + 1):
            # If the current square has not been painted, increment the number of ways to paint it
            if j not in painted:
                num_ways_range *= x

        # Multiply the number of ways to paint the current range by the total number of ways to paint the previous ranges
        num_ways *= num_ways_range

    # Return the number of ways to paint the squares modulo 10^9+7
    return num_ways % 1000000007

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(paint_squares(N, M, conditions))

