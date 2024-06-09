
def get_maximal_influence(n, spectators):
    # Sort the spectators by influence in descending order
    spectators.sort(key=lambda x: x[1], reverse=True)

    # Initialize variables to keep track of the selected spectators
    selected_spectators = []
    total_influence = 0
    alice_support = 0
    bob_support = 0

    # Iterate through the spectators and select them based on their political views
    for spectator in spectators:
        if spectator[0] == "11":  # Both Alice and Bob
            selected_spectators.append(spectator)
            total_influence += spectator[1]
            alice_support += 1
            bob_support += 1
        elif spectator[0] == "10":  # Alice but not Bob
            selected_spectators.append(spectator)
            total_influence += spectator[1]
            alice_support += 1
        elif spectator[0] == "01":  # Bob but not Alice
            selected_spectators.append(spectator)
            total_influence += spectator[1]
            bob_support += 1
        elif spectator[0] == "00":  # Neither Alice nor Bob
            continue

        # Check if we have selected at least half of the spectators who support Alice and at least half of the spectators who support Bob
        if alice_support >= n / 2 and bob_support >= n / 2:
            break

    # If we have selected at least half of the spectators who support Alice and at least half of the spectators who support Bob, return the total influence
    if alice_support >= n / 2 and bob_support >= n / 2:
        return total_influence
    else:
        return 0


n = int(input())
spectators = []

# Read the input and convert it to a list of tuples (political view, influence)
for i in range(n):
    political_view, influence = input().split()
    spectators.append((political_view, int(influence)))

# Call the function to get the maximal influence and print the result
result = get_maximal_influence(n, spectators)
print(result)

