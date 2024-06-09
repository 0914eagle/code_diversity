
def solve(n, permutation, sequence):
    # Initialize a list to store the number of visits for each position
    visits = [0] * (2 * n)

    # Iterate through the permutation and sequence
    for i in range(n):
        # Get the current position and the next position
        current_position = permutation[i]
        next_position = permutation[(i + 1) % n]

        # If the current position is not visited, visit it
        if visits[current_position] == 0:
            visits[current_position] = 1

        # If the next position is not visited, visit it
        if visits[next_position] == 0:
            visits[next_position] = 1

        # If the sequence is 1, reverse the current position
        if sequence[i] == 1:
            current_position = n - current_position

        # If the current position is not visited, visit it
        if visits[current_position] == 0:
            visits[current_position] = 1

    # Return the number of elements that need to be changed
    return sum(visits)

