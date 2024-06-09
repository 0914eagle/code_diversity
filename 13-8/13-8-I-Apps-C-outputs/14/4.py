
def solve(K, N):
    # Initialize a list to store the results
    results = []

    # Iterate over each possible sum
    for i in range(1, 2*K+1):
        # Initialize a set to store the combinations that satisfy the condition
        combinations = set()

        # Iterate over each possible combination of dice rolls
        for rolls in itertools.combinations(range(1, K+1), N):
            # Check if the sum of the rolls is equal to the current sum
            if sum(rolls) == i:
                # Add the combination to the set of combinations that satisfy the condition
                combinations.add(tuple(rolls))

        # Add the number of combinations that satisfy the condition to the results list
        results.append(len(combinations))

    # Return the results list
    return results

