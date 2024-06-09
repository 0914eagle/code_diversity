
def pistol_shooting(n, a):
    # Sort the cans in descending order of their durability
    sorted_cans = sorted(range(n), key=lambda i: a[i], reverse=True)

    # Initialize the number of shots required to knock down each can
    shots_required = [0] * n

    # Iterate through the cans in the sorted order
    for i in sorted_cans:
        # Calculate the number of shots required to knock down the current can
        shots_required[i] = sum(a[j] * shots_required[j] for j in range(n) if j != i) + 1

    # Return the minimum number of shots required to knock down each can
    # and the order of shooting
    return min(shots_required), sorted_cans

