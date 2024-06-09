
def get_wcd(pairs):
    # Initialize a set to store the common divisors
    common_divisors = set()
    
    # Iterate over the pairs
    for a, b in pairs:
        # Get the common divisors of a and b
        common_divisors |= set(range(2, min(a, b) + 1))
    
    # Return the largest common divisor
    return max(common_divisors) if common_divisors else -1

