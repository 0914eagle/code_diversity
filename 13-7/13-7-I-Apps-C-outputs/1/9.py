
def solve(m, h1, a1, x1, y1, h2, a2, x2, y2):
    # Initialize the minimum time as 0
    min_time = 0

    # Check if the initial heights are already equal to the desired heights
    if h1 == a1 and h2 == a2:
        return min_time

    # Check if the initial heights are not equal to the desired heights
    while h1 != a1 or h2 != a2:
        # Increment the minimum time by 1
        min_time += 1

        # Calculate the new heights of Xaniar and Abol
        h1 = (x1 * h1 + y1) % m
        h2 = (x2 * h2 + y2) % m

        # Check if the new heights are equal to the desired heights
        if h1 == a1 and h2 == a2:
            return min_time

    # If the minimum time is not returned yet, it means that the heights will never be equal to the desired heights
    return -1

