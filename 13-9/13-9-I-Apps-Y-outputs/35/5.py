
def sabotage(N):
    # Initialize a list to store the cuts
    cuts = []

    # Add horizontal cuts
    for i in range(N):
        cuts.append([i, 0])
        cuts.append([i, 1])

    # Add vertical cuts
    for i in range(N):
        cuts.append([0, i])
        cuts.append([1, i])

    # Return the length of the cuts list, which is the maximum number of pieces the chessboard can crash into
    return len(cuts)

