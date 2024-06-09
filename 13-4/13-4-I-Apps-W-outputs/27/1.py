
def get_min_m(n, k):
    # Initialize the minimum m as the maximum value of the given integers
    m = n * (n + 1) // 2
    
    # Iterate through all possible values of m
    for m in range(n, m + 1):
        # Initialize a set to store the integers used in the sets
        used_integers = set()
        # Initialize a list to store the sets
        sets = []
        # Iterate through the given integers
        for i in range(1, m + 1):
            # Check if the integer is not already used in any set
            if i not in used_integers:
                # Add the integer to the set
                sets.append(i)
                # Add the integer to the used integers set
                used_integers.add(i)
                # Check if the set has the required rank
                if len(sets) == n and all(gcd(x, y) == k for x, y in combinations(sets, 2)):
                    # If the set has the required rank, return the minimum m
                    return m
    # If no set with the required rank is found, return -1
    return -1

