
def find_nearest_fraction(x, y, n):
    # Initialize the minimum difference and the corresponding fraction
    min_diff = float('inf')
    nearest_frac = ''

    # Iterate through all possible denominators
    for b in range(1, n + 1):
        # Find the numerator that minimizes the difference
        a = round(x * b / y)

        # Calculate the difference between the given fraction and the current fraction
        diff = abs(x / y - a / b)

        # If the difference is less than the minimum difference, update the minimum difference and the corresponding fraction
        if diff < min_diff:
            min_diff = diff
            nearest_frac = f'{a}/{b}'

    # Return the nearest fraction
    return nearest_frac

