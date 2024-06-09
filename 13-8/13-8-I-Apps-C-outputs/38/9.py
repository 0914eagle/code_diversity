
def solve(offers):
    # Sort the offers by the first section of each offer
    offers.sort(key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize a set to keep track of the colors that have been used
    colors = set()

    # Loop through the offers and accept them if they can be accepted
    for offer in offers:
        # Check if the color of the offer has not been used before
        if offer[0] not in colors:
            # If the color has not been used before, increase the number of colors
            num_colors += 1

        # Add the color to the set of used colors
        colors.add(offer[0])

        # Check if the last section of the offer has not been painted before
        if offer[2] > num_sections:
            # If the last section has not been painted before, increase the number of sections painted
            num_sections = offer[2]

        # Check if the number of colors is less than or equal to 3
        if num_colors <= 3:
            # If the number of colors is less than or equal to 3, return the number of offers accepted
            return len(offers[:offers.index(offer) + 1])

    # If all the offers have been checked and the number of colors is still greater than 3, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

