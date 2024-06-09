
def get_nearest_fraction(x, y, n):
    # Initialize the minimum difference to a large value
    min_diff = 1e9
    # Initialize the minimum denominator to 0
    min_denom = 0
    # Iterate through all possible denominators
    for denom in range(1, n+1):
        # Calculate the numerator that is closest to x/y
        num = round(x*denom/y)
        # Calculate the absolute difference between the current fraction and x/y
        diff = abs(x*denom/y - num/denom)
        # If the difference is smaller than the minimum difference, update the minimum difference and denominator
        if diff < min_diff:
            min_diff = diff
            min_denom = denom
    # Return the fraction with the minimum denominator
    return str(min_denom) + "/" + str(min_denom)

