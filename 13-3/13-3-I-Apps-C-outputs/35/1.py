
def get_max_influence(n, spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0
    total_influence = 0

    # Iterate through the sorted spectators
    for spectator in spectators:
        # If the current spectator supports Alice, increment the Alice count
        if spectator[0] == "11" or spectator[0] == "10":
            alice_count += 1
        # If the current spectator supports Bob, increment the Bob count
        if spectator[0] == "11" or spectator[0] == "01":
            bob_count += 1
        # Add the influence of the current spectator to the total influence
        total_influence += spectator[1]

        # If the current spectator supports both Alice and Bob, we have found the optimal solution
        if alice_count > n / 2 and bob_count > n / 2:
            return total_influence

    # If we reach this point, it is impossible to select a non-empty set of spectators that supports both Alice and Bob
    return 0

