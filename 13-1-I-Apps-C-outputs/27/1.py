
def solve(n, colors, forbidden, sequence):
    # Initialize a list to store the number of arrangements for each length of sequence
    arrangements = [0] * (len(sequence) + 1)
    arrangements[0] = 1

    # Iterate over the length of the sequence
    for i in range(1, len(sequence) + 1):
        # Initialize a list to store the number of arrangements for each color
        color_arrangements = [0] * (n + 1)

        # Iterate over the previous length of sequence
        for j in range(i - 1):
            # Get the current color and the previous color
            current_color = sequence[j]
            previous_color = sequence[j - 1]

            # If the current color is not the same as the previous color and they are not forbidden to be next to each other
            if current_color != previous_color and (current_color, previous_color) not in forbidden:
                # Increment the number of arrangements for the current color
                color_arrangements[current_color] += arrangements[j]

        # Add the number of arrangements for the current color to the total number of arrangements
        arrangements[i] += sum(color_arrangements)

    # Return the total number of arrangements
    return arrangements[len(sequence)]

