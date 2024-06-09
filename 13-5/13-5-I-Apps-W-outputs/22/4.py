
def solve(n, permutation, sequence):
    # Initialize a dictionary to store the number of visits for each position
    visits = {i: 0 for i in range(1, n + 1)}

    # Iterate through the permutation and sequence
    for i in range(n):
        # Get the current position and the next position
        curr_pos = permutation[i]
        next_pos = permutation[(i + 1) % n]

        # If the current position is not the same as the next position, visit the current position
        if curr_pos != next_pos:
            visits[curr_pos] += 1

        # If the sequence is 1, visit the current position in the reversed direction
        if sequence[i] == 1:
            visits[next_pos] += 1

    # Calculate the minimum number of elements to change
    min_elements = 0
    for pos, count in visits.items():
        if count < 2:
            min_elements += 2 - count

    return min_elements

