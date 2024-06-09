
def get_max_influence(n, spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0
    total_influence = 0

    # Iterate through the sorted list of spectators
    for spectator in spectators:
        # If the current spectator supports Alice, increment the count
        if spectator[0] in ["11", "10"]:
            alice_count += 1
        # If the current spectator supports Bob, increment the count
        if spectator[0] in ["11", "01"]:
            bob_count += 1
        # Add the influence of the current spectator to the total influence
        total_influence += spectator[1]

        # If the current spectator supports both Alice and Bob, break the loop
        if spectator[0] == "11":
            break

    # Check if at least half of the spectators support Alice and at least half of them support Bob
    if alice_count >= n / 2 and bob_count >= n / 2:
        return total_influence
    else:
        return 0


n = int(input())
spectators = []

# Read the input and convert it to a list of tuples (political view, influence)
for i in range(n):
    political_view, influence = input().split()
    spectators.append((political_view, int(influence)))

# Call the get_max_influence function and print the result
print(get_max_influence(n, spectators))

