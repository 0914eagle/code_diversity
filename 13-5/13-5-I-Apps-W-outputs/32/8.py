
def solve(n, s, q, l, r):
    # Initialize a set to store the unique pitches
    pitches = set()

    # Iterate over each string
    for i in range(n):
        # Iterate over each fret
        for j in range(l[i], r[i] + 1):
            # Add the pitch to the set
            pitches.add(s[i] + j)

    # Return the length of the set
    return len(pitches)

