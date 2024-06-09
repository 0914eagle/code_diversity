
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
        if spectator[0] in ["11", "10"]:
            alice_count += 1
        # If the current spectator supports Bob, increment the Bob count
        if spectator[0] in ["11", "01"]:
            bob_count += 1
        # Add the influence of the current spectator to the total influence
        total_influence += spectator[1]

        # If the current spectator supports both Alice and Bob, break the loop
        if spectator[0] == "11":
            break

    # If at least half of the spectators support Alice and at least half of the spectators support Bob, return the total influence
    if alice_count >= n / 2 and bob_count >= n / 2:
        return total_influence
    else:
        return 0


n = int(input())
spectators = []

# Iterate through the next n lines of input
for i in range(n):
    # Split the input into the political view and influence
    political_view, influence = input().split()
    # Add the political view and influence to the list of spectators
    spectators.append([political_view, int(influence)])

# Call the get_max_influence function and print the result
print(get_max_influence(n, spectators))

