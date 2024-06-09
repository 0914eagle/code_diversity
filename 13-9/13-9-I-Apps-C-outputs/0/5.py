
def get_maximal_total_influence(n, spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the number of spectators supporting Alice and Bob
    alice_count = 0
    bob_count = 0

    # Initialize a variable to keep track of the total influence
    total_influence = 0

    # Iterate through the sorted list of spectators
    for spectator in spectators:
        # If the spectator supports Alice, increment the count
        if spectator[0] in ["11", "10"]:
            alice_count += 1
        # If the spectator supports Bob, increment the count
        if spectator[0] in ["11", "01"]:
            bob_count += 1
        # Add the influence of the current spectator to the total influence
        total_influence += spectator[1]

        # If the total influence is greater than or equal to half of the number of spectators and at least half of the spectators support Alice and Bob, return the total influence
        if total_influence >= n / 2 and alice_count >= n / 4 and bob_count >= n / 4:
            return total_influence

    # If we reach this point, it is impossible to select a non-empty set of spectators with at least half supporting Alice and Bob, so return 0
    return 0


n = int(input())
spectators = []

# Read the input and convert it to a list of tuples (political views, influence)
for i in range(n):
    views, influence = input().split()
    spectators.append((views, int(influence)))

# Call the function to get the maximal total influence
result = get_maximal_total_influence(n, spectators)

# Print the result
print(result)

