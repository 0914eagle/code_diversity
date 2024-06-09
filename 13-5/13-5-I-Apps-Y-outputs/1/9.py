
def solve(n, k):
    # Initialize a list to store the colors of the costumes
    colors = []

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # If i is even, assign the color as (i % k) + 1
        if i % 2 == 0:
            colors.append((i % k) + 1)
        # If i is odd, assign the color as k - (i % k) + 1
        else:
            colors.append(k - (i % k) + 1)

    # Return the colors list
    return colors

