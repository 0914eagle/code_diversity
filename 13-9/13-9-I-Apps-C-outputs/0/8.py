
def get_maximum_total_influence(n, spectators):
    # Sort the spectators by their influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0

    # Initialize a variable to keep track of the total influence
    total_influence = 0

    # Iterate through the sorted list of spectators
    for spectator in spectators:
        # Check if the current spectator supports Alice
        if spectator[0] == "11" or spectator[0] == "10":
            # Increment the number of spectators supporting Alice
            alice_count += 1

        # Check if the current spectator supports Bob
        if spectator[0] == "11" or spectator[0] == "01":
            # Increment the number of spectators supporting Bob
            bob_count += 1

        # Check if the current spectator supports both Alice and Bob
        if spectator[0] == "11":
            # Increment the total influence by the influence of the current spectator
            total_influence += spectator[1]

    # Check if at least half of the spectators support Alice and at least half of the spectators support Bob
    if alice_count >= n / 2 and bob_count >= n / 2:
        # Return the total influence
        return total_influence
    else:
        # Return 0 since it is impossible to select a non-empty set of spectators that satisfy the conditions
        return 0


n = int(input())
spectators = []

# Iterate through the next n lines of input
for i in range(n):
    # Split the current line into the political views and influence
    political_views, influence = input().split()
    # Add the current spectator to the list of spectators
    spectators.append((political_views, int(influence)))

# Call the get_maximum_total_influence function and print the result
print(get_maximum_total_influence(n, spectators))

