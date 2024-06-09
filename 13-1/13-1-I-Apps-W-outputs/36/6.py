
def solve(N, D, A, X_H):
    # Sort the monsters by their coordinates
    X_H.sort(key=lambda x: x[0])

    # Initialize the number of bombs needed to 0
    bombs_needed = 0

    # Loop through the monsters
    for i in range(N):
        # Get the current monster's coordinate and health
        x, h = X_H[i]

        # If the monster's health is already 0 or below, skip it
        if h <= 0:
            continue

        # Calculate the range of coordinates that the bomb can affect
        range_start = max(x - D, 0)
        range_end = min(x + D, 10**9)

        # Loop through the monsters in the affected range
        for j in range(i, N):
            # Get the current monster's coordinate and health
            x_j, h_j = X_H[j]

            # If the monster's coordinate is outside the range, break the loop
            if x_j < range_start or x_j > range_end:
                break

            # Decrease the monster's health by the bomb's attack power
            h_j -= A

            # If the monster's health becomes 0 or below, break the loop
            if h_j <= 0:
                break

        # If the monster's health becomes 0 or below, increase the number of bombs needed
        if h <= 0:
            bombs_needed += 1

    # Return the minimum number of bombs needed to win
    return bombs_needed

