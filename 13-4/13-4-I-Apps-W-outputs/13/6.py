
def solve(n, m, f, b):
    # Initialize a dictionary to store the counts of each number
    counts = {}
    for i in range(n):
        counts[i+1] = 0
    # Loop through the f and b sequences and update the counts
    for i in range(m):
        counts[f[i]] += 1
        counts[b[i]] -= 1
    # Check if the counts are all zero, which means the sequences are possible
    if all(count == 0 for count in counts.values()):
        return "Possible"
    # Check if the counts are not all zero and there is only one possible sequence, which means the sequences are ambiguous
    possible_sequences = []
    for key, value in counts.items():
        if value != 0:
            possible_sequences.append(key)
    if len(possible_sequences) == 1:
        return "Ambiguity"
    # If the counts are not all zero and there is not only one possible sequence, which means the sequences are impossible
    return "Impossible"

