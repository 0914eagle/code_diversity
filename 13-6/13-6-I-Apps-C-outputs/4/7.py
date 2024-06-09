
def solve(n):
    # Initialize a list to store the swaps
    swaps = []

    # Iterate through all possible pairs of positions
    for i in range(n):
        for j in range(i+1, n):
            # If the positions are not already swapped, swap them
            if i != j:
                swaps.append([i, j])

    # If the length of the swaps list is equal to the number of pairs of positions,
    # it means that all pairs of positions can be swapped to stay the same
    if len(swaps) == n * (n - 1) // 2:
        return "YES\n" + "\n".join([f"{swap[0]} {swap[1]}" for swap in swaps])
    else:
        return "NO"

