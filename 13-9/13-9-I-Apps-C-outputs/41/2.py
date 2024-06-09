
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the current color and section
    current_color = ""
    current_section = 0

    # Initialize the number of offers accepted
    num_accepted = 0

    # Loop through the sorted offers
    for offer in sorted_offers:
        # If the current color is not the same as the color in the current offer, we need to accept the current offer
        if current_color != offer[0]:
            num_accepted += 1
            current_color = offer[0]

        # If the current section is not the same as the section in the current offer, we need to accept the current offer
        if current_section != offer[1]:
            num_accepted += 1
            current_section = offer[1]

        # If we have accepted more than 3 colors, it is impossible to satisfy the requirements
        if num_accepted > 3:
            return "IMPOSSIBLE"

    # If we have accepted all the offers, return the number of offers accepted
    return num_accepted

