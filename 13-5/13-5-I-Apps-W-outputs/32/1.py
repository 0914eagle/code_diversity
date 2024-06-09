
def solve(n, s, q, lr):
    # Initialize a set to store the unique pitches
    pitches = set()

    # Iterate over each string
    for i in range(n):
        # Get the tuning of the string
        tuning = s[i]

        # Iterate over each fret
        for j in range(lr[0], lr[1] + 1):
            # Add the pitch to the set
            pitches.add(tuning + j)

    # Return the length of the set
    return len(pitches)

