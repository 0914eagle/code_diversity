
def get_maximum_influence(spectators):
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
        if spectator[0] == "11" or spectator[0] == "10":
            # Increment the number of spectators supporting Alice
            alice_count += 1

        # Check if the current spectator supports Bob
        if spectator[0] == "11" or spectator[0] == "01":
            # Increment the number of spectators supporting Bob
            bob_count += 1

        # Add the influence of the current spectator to the total influence
        total_influence += spectator[1]

        # Check if the current spectator supports both Alice and Bob
        if spectator[0] == "11":
            # If the current spectator supports both Alice and Bob, break the loop
            break

    # Check if at least half of the spectators support Alice and at least half of the spectators support Bob
    if alice_count >= len(spectators) / 2 and bob_count >= len(spectators) / 2:
        # Return the total influence
        return total_influence
    else:
        # Return 0 if it is impossible to select a set of spectators that support both Alice and Bob
        return 0


# Main function
if __name__ == "__main__":
    # Read the number of spectators from stdin
    n = int(input())

    # Read the information about each spectator from stdin
    spectators = []
    for i in range(n):
        spectrum = input().split()
        spectators.append((spectrum[0], int(spectrum[1])))

    # Call the function to get the maximum influence
    result = get_maximum_influence(spectators)

    # Print the result
    print(result)

