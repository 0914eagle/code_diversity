
def solve(K, N):
    # Initialize a list to store the results
    results = []

    # Loop through each possible sum
    for i in range(1, 2*K+1):
        # Initialize a set to store the combinations that satisfy the condition
        combinations = set()

        # Loop through each possible combination of dice
        for dice in itertools.combinations(range(1, K+1), N):
            # Check if the sum of the dice is equal to the current sum
            if sum(dice) == i:
                # Add the combination to the set
                combinations.add(tuple(dice))

        # Add the number of combinations to the results list
        results.append(len(combinations))

    # Return the results list
    return results

