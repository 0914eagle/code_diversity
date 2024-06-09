
def get_maximal_total_influence(n, spectators):
    # Sort the spectators by their influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0
    total_influence = 0

    # Iterate through the sorted list of spectators
    for spectator in spectators:
        # If the current spectator supports Alice, increment Alice count
        if spectator[0] in ["11", "10"]:
            alice_count += 1
        # If the current spectator supports Bob, increment Bob count
        if spectator[0] in ["11", "01"]:
            bob_count += 1
        # Add the current spectator's influence to the total influence
        total_influence += spectator[1]

        # If both Alice and Bob have at least half of the spectators, return the total influence
        if alice_count >= n / 2 and bob_count >= n / 2:
            return total_influence

    # If it is not possible to select a non-empty set of spectators satisfying the conditions, return 0
    return 0


n = int(input())
spectators = []

# Iterate through the next n lines of input
for i in range(n):
    # Split the current line into the political view and influence
    political_view, influence = input().split()
    # Add the current spectator to the list of spectators
    spectators.append([political_view, int(influence)])

# Call the get_maximal_total_influence function and print the result
print(get_maximal_total_influence(n, spectators))

