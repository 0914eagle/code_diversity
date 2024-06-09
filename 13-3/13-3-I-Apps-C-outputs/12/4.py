
import sys

def paint_squares(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for i in range(M):
        # Get the left and right indices, and the number of different colors
        l, r, x = conditions[i]

        # Calculate the number of ways to paint the squares with the current condition
        num_ways *= comb(r - l + 1, x)

        # Modulo the result to avoid overflow
        num_ways %= 1000000007

    # Return the number of ways to paint the squares
    return num_ways

def comb(n, r):
    # Calculate the binomial coefficient (n choose r)
    if r > n - r:
        r = n - r
    if r == 0:
        return 1
    else:
        num = 1
        for i in range(r):
            num *= n - i
            num //= i + 1
        return num

if __name__ == '__main__':
    # Read the input from stdin
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))

    # Call the paint_squares function and print the result
    print(paint_squares(N, M, conditions))

