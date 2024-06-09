
def get_maximum_total_influence(spectators):
    # Sort the spectators by their influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0

    # Initialize a variable to keep track of the total influence
    total_influence = 0

    # Iterate through the spectators
    for spectator in spectators:
        # Get the political view and influence of the current spectator
        view, influence = spectator[0], spectator[1]

        # Check if the current spectator supports Alice
        if view == "11" or view == "10":
            # Increment the count of spectators supporting Alice
            alice_count += 1

        # Check if the current spectator supports Bob
        if view == "11" or view == "01":
            # Increment the count of spectators supporting Bob
            bob_count += 1

        # Check if the current spectator supports both Alice and Bob
        if view == "11":
            # Increment the total influence by the influence of the current spectator
            total_influence += influence

    # Check if at least half of the spectators support Alice and at least half of them support Bob
    if alice_count >= len(spectators) // 2 and bob_count >= len(spectators) // 2:
        # Return the total influence
        return total_influence
    else:
        # Return 0 as the total influence is not maximized
        return 0

