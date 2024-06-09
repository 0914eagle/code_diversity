
def get_maximal_influence(n, spectators):
    # Sort the spectators by influence in descending order
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

        # Add the current spectator to the selected spectators list
        selected_spectators.append(spectator)
        total_influence += spectator[1]

        # Check if the conditions for selecting the current spectator are met
        if alice_support >= n / 2 and bob_support >= n / 2:
            break

    # Check if it is possible to select at least half of the spectators who support Alice and at least half of the spectators who support Bob
    if alice_support < n / 2 or bob_support < n / 2:
        return 0

    return total_influence

