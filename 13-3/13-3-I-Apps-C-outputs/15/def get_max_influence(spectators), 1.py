
def get_max_influence(spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0

    # Initialize a variable to keep track of the total influence
    total_influence = 0

    # Iterate through the spectators
    for spectator in spectators:
        # Check if the current spectator supports Alice
        if spectator[0] in ["11", "10"]:
            alice_count += 1

        # Check if the current spectator supports Bob
        if spectator[0] in ["11", "01"]:
            bob_count += 1

        # Add the influence of the current spectator to the total influence
        total_influence += spectator[1]

        # Check if at least half of the spectators support Alice and at least half of them support Bob
        if alice_count >= len(spectators) / 2 and bob_count >= len(spectators) / 2:
            return total_influence

    # If we reach this point, it means that it is impossible to select a non-empty set of spectators that satisfies the conditions
    return 0

