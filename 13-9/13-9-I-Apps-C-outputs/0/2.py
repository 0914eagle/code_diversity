
def get_max_influence(spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0

    # Initialize a variable to keep track of the total influence
    total_influence = 0

    # Iterate through the spectators and select the ones that support Alice and Bob
    for spectator in spectators:
        if spectator[0] == "11" or spectator[0] == "10":
            alice_count += 1
        if spectator[0] == "11" or spectator[0] == "01":
            bob_count += 1
        total_influence += spectator[1]

        # If we have selected at least half of the spectators supporting Alice and Bob, break the loop
        if alice_count >= len(spectators) // 2 and bob_count >= len(spectators) // 2:
            break

    # If we have selected at least half of the spectators supporting Alice and Bob, return the total influence
    if alice_count >= len(spectators) // 2 and bob_count >= len(spectators) // 2:
        return total_influence
    else:
        return 0

