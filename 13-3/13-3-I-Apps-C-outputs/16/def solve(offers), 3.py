
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize a set to store the colors that have been used
    colors = set()

    # Loop through the sorted offers and accept them if they can be painted
    for offer in sorted_offers:
        # Check if the color of the offer has not been used before
        if offer[0] not in colors:
            # If the color has not been used before, increment the number of colors
            num_colors += 1

        # Add the color to the set of used colors
        colors.add(offer[0])

        # Check if the number of sections painted is less than the total number of sections
        if num_sections < 10000:
            # If the number of sections painted is less than the total number of sections, increment the number of sections
            num_sections += 1

        # Check if the number of colors is less than or equal to 3
        if num_colors <= 3:
            # If the number of colors is less than or equal to 3, accept the offer
            continue
        else:
            # If the number of colors is greater than 3, break the loop and return the number of offers accepted
            break

    # Check if all the sections have been painted
    if num_sections == 10000:
        # If all the sections have been painted, return the number of offers accepted
        return len(offers[:i])
    else:
        # If not all the sections have been painted, return "IMPOSSIBLE"
        return "IMPOSSIBLE"

