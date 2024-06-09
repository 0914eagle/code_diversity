
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors required
        l, r, x = conditions[i]

        # Calculate the number of ways to paint the squares with the current condition
        num_ways *= (r - l + 1) - (x - 1)

        # Modulo the result to avoid overflow
        num_ways %= 1000000007

    # Return the number of ways to paint the squares
    return num_ways

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(paint_squares(N, M, conditions))

