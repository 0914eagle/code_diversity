
def get_max_birds(l, d, n, positions):
    # Sort the positions of the birds
    sorted_positions = sorted(positions)

    # Initialize the number of additional birds that can sit on the wire
    max_birds = 0

    # Iterate through the positions of the birds
    for i in range(n):
        # Check if the current position is at least 6 cm from the poles and at least d cm from the previous bird
        if sorted_positions[i] >= 6 and sorted_positions[i] - sorted_positions[i-1] >= d:
            max_birds += 1

    return max_birds

