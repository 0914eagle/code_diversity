
def solve(n, b):
    # Check if the given sequence is increasing
    if all(b[i] < b[i+1] for i in range(n-1)):
        return "Yes\n" + " ".join(str(x) for x in b)

    # Check if the given sequence can be shuffled to form an increasing sequence
    shuffled_sequence = list(b)
    shuffled_sequence.sort()
    if all(shuffled_sequence[i] < shuffled_sequence[i+1] for i in range(n-1)):
        return "Yes\n" + " ".join(str(x) for x in shuffled_sequence)

    # If no valid permutation exists, return "No"
    return "No"

