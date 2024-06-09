
def find_nearest_fraction(x, y, n):
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    # Initialize the minimum denominator to 0
    min_denominator = 0
    # Iterate through all possible denominators from 1 to n
    for denominator in range(1, n + 1):
        # Find the numerator that is closest to x/y for the current denominator
        numerator = round(x * denominator / y)
        # Calculate the absolute difference between the current fraction and x/y
        diff = abs(numerator / denominator - x / y)
        # If the difference is smaller than the minimum difference, update the minimum difference and numerator
        if diff < min_diff:
            min_diff = diff
            min_numerator = numerator
            min_denominator = denominator
    # Return the fraction with the minimum denominator and numerator
    return f"{min_numerator}/{min_denominator}"

