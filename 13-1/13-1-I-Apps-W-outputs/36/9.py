
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
        range_low = max(x - D, 0)
        range_high = min(x + D, 10**9)

        # Loop through the monsters in the range
        for j in range(i, N):
            # Get the current monster's coordinate and health
            x_j, h_j = X_H[j]

            # If the monster's coordinate is outside the range, break
            if x_j < range_low or x_j > range_high:
                break

            # Decrease the monster's health by the bomb's power
            h_j -= A

            # If the monster's health becomes 0 or below, break
            if h_j <= 0:
                break

        # Increment the number of bombs needed
        bombs_needed += 1

    # Return the number of bombs needed
    return bombs_needed

