
def solve(n, s, q, lr):
    # Initialize a set to store the unique pitches
    pitches = set()

    # Iterate over each question
    for l, r in lr:
        # Iterate over each string
        for i in range(n):
            # Add the pitches for the current string between the given range to the set
            pitches.update(s[i] + j for j in range(l, r + 1))

        # Return the length of the set, which is the number of unique pitches
        return len(pitches)

