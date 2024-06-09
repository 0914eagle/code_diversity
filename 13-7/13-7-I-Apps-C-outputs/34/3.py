
def solve(n, k, partners):
    # Sort the partners by their Frag and Step values
    partners.sort(key=lambda x: (x[0], x[1]))

    # Initialize the maximum diversity to 0
    max_diversity = 0

    # Initialize the current diversity to 0
    current_diversity = 0

    # Iterate through the partners
    for i in range(n):
        # If the current partner can be awakened
        if partners[i][2] != 0:
            # Increment the current diversity
            current_diversity += 1

            # If the current diversity is greater than the maximum diversity
            if current_diversity > max_diversity:
                # Update the maximum diversity
                max_diversity = current_diversity

            # If the current diversity is equal to the maximum diversity and the current partner is not the first partner in the list
            elif current_diversity == max_diversity and i != 0:
                # Decrement the current diversity
                current_diversity -= 1

                # Increment the maximum diversity
                max_diversity += 1

    # Return the maximum diversity
    return max_diversity

