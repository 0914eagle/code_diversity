
def solve(n, a):
    # Initialize a dictionary to map each kid to its remembered kids
    remembered = {i: set() for i in range(1, n + 1)}
    for i in range(n):
        remembered[i + 1].add(a[i][0])
        remembered[i + 1].add(a[i][1])

    # Initialize a set to store the kids that have been processed
    processed = set()

    # Initialize the permutation with the first kid
    permutation = [1]

    # Loop until all kids have been processed
    while len(processed) < n:
        # Get the current kid and its remembered kids
        current_kid = permutation[-1]
        current_remembered = remembered[current_kid]

        # Find the next kid that is not in the permutation and is remembered by the current kid
        for next_kid in current_remembered:
            if next_kid not in processed:
                break
        else:
            # If no such kid is found, find the first kid that is not in the permutation
            for next_kid in range(1, n + 1):
                if next_kid not in processed:
                    break

        # Add the next kid to the permutation and mark it as processed
        permutation.append(next_kid)
        processed.add(next_kid)

    return permutation

