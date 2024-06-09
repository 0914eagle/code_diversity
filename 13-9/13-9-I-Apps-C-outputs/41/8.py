
def solve(offers):
    # Sort the offers by the first section of each offer
    offers.sort(key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize a set to store the colors that have been used
    colors = set()

    # Loop through the offers
    for offer in offers:
        # Check if the offer can be accepted
        if num_sections + offer[2] - offer[1] + 1 <= 10000 and num_colors + 1 <= 3:
            # Accept the offer
            num_sections += offer[2] - offer[1] + 1
            num_colors += 1
            colors.add(offer[0])
        else:
            # If the offer cannot be accepted, return "IMPOSSIBLE"
            return "IMPOSSIBLE"

    # If all sections have been painted and at most 3 colors have been used, return the number of offers accepted
    return len(offers)

