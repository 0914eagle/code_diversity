
def get_max_additional_birds(l, d, n, positions):
    # Sort the positions of the birds already on the wire
    sorted_positions = sorted(positions)

    # Initialize the maximum number of additional birds to 0
    max_additional_birds = 0

    # Iterate over the positions of the birds already on the wire
    for i in range(n):
        # Get the position of the current bird
        current_position = sorted_positions[i]

        # Check if the current position is within the allowed distance from the pole
        if current_position < 6 or current_position > l - 6:
            continue

        # Check if the current position is within the allowed distance from the previous bird
        if i > 0 and current_position - sorted_positions[i - 1] < d:
            continue

        # Increment the maximum number of additional birds
        max_additional_birds += 1

    return max_additional_birds

