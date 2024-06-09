
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize a set to store the colors that have been used
    used_colors = set()

    # Loop through the sorted offers and accept them if they can be accepted
    for offer in sorted_offers:
        color, first_section, last_section = offer

        # If the color has not been used before, increment the number of colors
        if color not in used_colors:
            num_colors += 1
            used_colors.add(color)

        # Increment the number of sections painted
        num_sections += last_section - first_section + 1

        # If the number of colors is greater than 3, return "IMPOSSIBLE"
        if num_colors > 3:
            return "IMPOSSIBLE"

    # If all the sections have been painted, return the number of offers accepted
    if num_sections == 10000:
        return len(offers)

    # If not all the sections have been painted, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

