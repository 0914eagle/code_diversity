
def get_maximal_influence(n, spectators):
    # Sort the spectators by their influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the selected spectators
    selected_spectators = []
    total_influence = 0
    alice_support = 0
    bob_support = 0

    # Iterate through the sorted spectators
    for spectator in spectators:
        # Check if the current spectator supports Alice
        if spectator[0] in ["11", "10"]:
            alice_support += 1

        # Check if the current spectator supports Bob
        if spectator[0] in ["11", "01"]:
            bob_support += 1

        # Check if the current spectator supports both Alice and Bob
        if spectator[0] == "11":
            alice_support += 1
            bob_support += 1

        # Check if the current spectator supports neither Alice nor Bob
        if spectator[0] == "00":
            continue

        # Add the current spectator to the selected spectators
        selected_spectators.append(spectator)
        total_influence += spectator[1]

        # Check if the selected spectators support at least half of the total number of spectators
        if len(selected_spectators) >= n // 2 and alice_support >= n // 4 and bob_support >= n // 4:
            return total_influence

    # If no combination of spectators supports at least half of the total number of spectators, return 0
    return 0

