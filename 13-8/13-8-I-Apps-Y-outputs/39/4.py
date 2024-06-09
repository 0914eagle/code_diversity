
def can_shooting(n, a):
    # Sort the cans in descending order of their durability
    sorted_cans = sorted(range(n), key=lambda i: a[i], reverse=True)

    # Initialize the number of shots required to knock down each can to infinity
    shots_required = [float("inf") for _ in range(n)]

    # Initialize the number of shots required to knock down the first can to 0
    shots_required[sorted_cans[0]] = 0

    # Loop through the remaining cans and calculate the minimum number of shots required to knock them down
    for i in range(1, n):
        for j in range(i):
            shots_required[sorted_cans[i]] = min(shots_required[sorted_cans[i]], shots_required[sorted_cans[j]] + a[sorted_cans[j]] * (i - j) + 1)

    # Return the minimum number of shots required to knock down each can and the order of shooting
    return shots_required, sorted_cans

