
def reconstruct_arrows(N, K, a):
    # Initialize a dictionary to map each person to their next position
    person_to_position = {i: i for i in range(1, N + 1)}
    for i in range(K):
        # Get the current position of each person
        current_positions = [person_to_position[i] for i in range(1, N + 1)]
        # Update the dictionary with the new positions
        for i in range(N):
            person_to_position[current_positions[i]] = a[current_positions[i] - 1]
    # Return the dictionary as a list of arrows
    return [person_to_position[i] for i in range(1, N + 1)]

