
def get_maximal_influence(n, spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0
    total_influence = 0

    # Iterate through the spectators and add them to the set if they support Alice or Bob
    for spectator in spectators:
        if spectator[0] == "11" or spectator[0] == "10":
            alice_count += 1
        if spectator[0] == "11" or spectator[0] == "01":
            bob_count += 1
        total_influence += spectator[1]

        # If we have at least half of the spectators supporting Alice and Bob, return the total influence
        if alice_count >= n / 2 and bob_count >= n / 2:
            return total_influence

    # If we reach this point, it is impossible to select a non-empty set of spectators with at least half supporting Alice and Bob
    return 0

