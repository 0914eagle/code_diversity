
def solve(n, permutation, sequence):
    # Initialize a list to store the number of visits for each position
    visits = [0] * (2 * n)

    # Iterate through the permutation and sequence
    for i in range(n):
        # Get the current position and the next position
        current = permutation[i]
        next = permutation[(i + 1) % n]

        # If the current position is not visited, visit it
        if visits[current] == 0:
            visits[current] = 1

        # If the next position is not visited, visit it
        if visits[next] == 0:
            visits[next] = 1

        # If the sequence is 1, reverse the current position
        if sequence[i] == 1:
            current = n - current + 1

        # If the current position is not visited, visit it
        if visits[current] == 0:
            visits[current] = 1

    # Return the number of unvisited positions
    return sum(visits)

