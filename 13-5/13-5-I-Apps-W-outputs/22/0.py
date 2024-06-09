
def solve(n, permutation, sequence):
    # Initialize a set to store the visited positions
    visited = set()
    # Initialize a variable to store the number of changes needed
    changes_needed = 0
    # Iterate through the permutation and sequence
    for i in range(n):
        # If the current position is not visited, mark it as visited and add it to the set
        if permutation[i] not in visited:
            visited.add(permutation[i])
        # If the current position is reversed, mark it as visited and add it to the set
        if sequence[i] == 1:
            visited.add(n - permutation[i] + 1)
        # If the number of visited positions is less than 2n, increment the number of changes needed
        if len(visited) < 2*n:
            changes_needed += 1
    # Return the number of changes needed
    return changes_needed

