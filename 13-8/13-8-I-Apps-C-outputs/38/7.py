
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize a set to keep track of the colors that have been used
    colors = set()

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # If the current offer does not overlap with any of the previous offers, accept it
        if offer[1] > num_sections:
            num_colors += 1
            colors.add(offer[0])
            num_sections = offer[2]
        # If the current offer overlaps with a previous offer, but does not use a new color, accept it
        elif offer[0] in colors:
            num_sections = offer[2]
        # If the current offer overlaps with a previous offer and uses a new color, reject it
        else:
            return "IMPOSSIBLE"

    # If all sections have been painted and no more than 3 colors have been used, return the number of accepted offers
    if num_sections == 10000 and num_colors <= 3:
        return len(sorted_offers)
    # Otherwise, return "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"

