
def can_knockdown_problem(n, a):
    # Sort the cans in descending order of durability
    sorted_cans = sorted(range(n), key=lambda i: a[i], reverse=True)

    # Initialize the number of shots required to knock down each can
    shots_required = [0] * n

    # Loop through the cans in descending order of durability
    for i in sorted_cans:
        # Add the number of shots required to knock down the current can
        shots_required[i] += sum(shots_required[:i]) + 1

    # Return the minimum number of shots required to knock down each can
    # and the order of cans in which they should be knocked down
    return min(shots_required), sorted_cans

