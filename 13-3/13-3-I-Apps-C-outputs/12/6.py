
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for l, r, x in conditions:
        # Calculate the number of ways to paint the current condition
        num_ways *= count_ways(N, l, r, x)

        # Modulo the result to avoid overflow
        num_ways %= 1000000007

    return num_ways

def count_ways(N, l, r, x):
    # Base case: if the range is empty, return 1
    if l > r:
        return 1

    # Initialize the number of ways to paint the current range
    num_ways = 0

    # Loop through each possible color
    for color in range(1, x + 1):
        # Calculate the number of ways to paint the current color
        num_ways += count_ways(N, l + 1, r, x - 1)

        # Modulo the result to avoid overflow
        num_ways %= 1000000007

    return num_ways

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(paint_squares(N, M, conditions))

