
def get_min_m(n, k):
    # Initialize the minimum m as the maximum value of n and k
    m = max(n, k)
    # Create a list to store the sets
    sets = []
    # Iterate through the numbers from 1 to m
    for i in range(1, m + 1):
        # Check if the number is divisible by k
        if i % k == 0:
            # Add the number to the set
            sets.append(i)
            # If the set has 4 elements, break the loop
            if len(sets) == n:
                break
    # Return the minimum m and the sets
    return m, sets

