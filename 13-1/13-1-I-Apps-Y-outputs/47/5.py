
def f1(N):
    # Initialize a list to store the positions of the cuts
    cuts = []

    # Iterate from 1 to N
    for i in range(1, N + 1):
        # Calculate the position of the cut
        pos = i * (8 / N)

        # Round the position to the nearest integer
        pos = int(round(pos))

        # Add the position to the list of cuts
        cuts.append(pos)

    # Return the length of the list of cuts
    return len(cuts)

