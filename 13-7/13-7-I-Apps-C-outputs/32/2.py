
def solve(n, k, x, rangers):
    # Sort the rangers in increasing order of strength
    rangers.sort()

    # Initialize the minimum and maximum strengths
    min_strength, max_strength = rangers[0], rangers[0]

    # Perform the operation k times
    for i in range(k):
        # Update the strength of each alternate ranger with x
        for j in range(1, n, 2):
            rangers[j] = rangers[j] ^ x

        # Update the minimum and maximum strengths
        min_strength = min(min_strength, rangers[0])
        max_strength = max(max_strength, rangers[-1])

    # Return the minimum and maximum strengths
    return [min_strength, max_strength]

