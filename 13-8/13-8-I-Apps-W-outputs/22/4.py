
def solve(c, t):
    if len(c) != len(t):
        return "No"
    if c == t:
        return "Yes"

    # Initialize the charges of the stones
    charges = c

    # Perform synchronization operations until the charges match
    while charges != t:
        # Find the index of the stone with the largest difference between its charge and the target charge
        max_diff_index = 0
        max_diff = abs(charges[0] - t[0])
        for i in range(1, len(charges)):
            diff = abs(charges[i] - t[i])
            if diff > max_diff:
                max_diff = diff
                max_diff_index = i

        # Synchronize the stone at the maximum difference index
        charges[max_diff_index] += charges[max_diff_index - 1] + charges[max_diff_index + 1] - charges[max_diff_index]

    # Check if the charges match after synchronization
    if charges == t:
        return "Yes"
    else:
        return "No"

