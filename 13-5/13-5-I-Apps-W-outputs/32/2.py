
def solve(n, s, q, l_r):
    # Initialize a set to store the unique pitches
    unique_pitches = set()

    # Iterate over each question
    for l, r in l_r:
        # Iterate over each string
        for i in range(n):
            # Add the pitches between l and r (inclusive) to the set
            unique_pitches |= set(s[i] + j for j in range(l, r + 1))

        # Return the length of the set
        yield len(unique_pitches)


