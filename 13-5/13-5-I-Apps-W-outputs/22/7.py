
def solve(n, permutation, sequence):
    # Initialize a set to store the visited positions
    visited = set()
    # Initialize a variable to store the number of changes needed
    changes_needed = 0
    # Loop through each position in the permutation
    for i in range(n):
        # If the current position is not visited, mark it as visited and add it to the set
        if permutation[i] not in visited:
            visited.add(permutation[i])
        # If the current position is visited and the corresponding element in the sequence is 1, reverse the position and add 1 to the number of changes needed
        elif sequence[i] == 1:
            permutation[i] = n - permutation[i] + 1
            changes_needed += 1
    # Return the number of changes needed
    return changes_needed

