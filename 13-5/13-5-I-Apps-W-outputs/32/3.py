
def solve(n, s, q, l_r):
    # Initialize a set to store the unique pitches
    pitches = set()

    # Loop through each question
    for l, r in l_r:
        # Loop through each string
        for i in range(n):
            # Add the pitches for the current string between the given range to the set
            pitches.update(s[i] + j for j in range(l, r + 1))

        # Return the number of unique pitches
        return len(pitches)

