
def solve(a, b, x):
    n = len(a)
    m = len(b)
    c = [[a[i] * b[j] for j in range(m)] for i in range(n)]

    # Initialize the maximum area to 0
    max_area = 0

    # Iterate over all possible positions of the top-left corner
    for i in range(n):
        for j in range(m):
            # Initialize the current area to 0
            current_area = 0

            # Iterate over all possible sizes of the subrectangle
            for k in range(i, n + 1):
                for l in range(j, m + 1):
                    # Calculate the current area
                    current_area += (k - i) * (l - j)

                    # If the current area is less than or equal to x and greater than the maximum area, update the maximum area
                    if current_area <= x and current_area > max_area:
                        max_area = current_area

    # Return the maximum area
    return max_area

