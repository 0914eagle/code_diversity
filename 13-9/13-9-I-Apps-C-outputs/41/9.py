
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])

    # Initialize the variables
    num_colors = 0
    num_sections = 0
    current_color = ""
    current_section = 0
    accepted_offers = 0

    # Iterate through the offers
    for offer in offers:
        # If the current color is empty, assign the current color to the first color in the offer
        if current_color == "":
            current_color = offer[0]

        # If the current color is the same as the current color in the offer, increase the number of sections
        elif current_color == offer[0]:
            num_sections += 1

        # If the current color is different from the current color in the offer, check if the number of sections is greater than 0
        else:
            # If the number of sections is greater than 0, increase the number of accepted offers
            if num_sections > 0:
                accepted_offers += 1

            # Reset the number of sections and the current color
            num_sections = 1
            current_color = offer[0]

        # If the number of colors is 3, return IMPOSSIBLE
        if num_colors == 3:
            return "IMPOSSIBLE"

        # Increase the number of colors
        num_colors += 1

    # If the number of sections is greater than 0, increase the number of accepted offers
    if num_sections > 0:
        accepted_offers += 1

    # Return the number of accepted offers
    return accepted_offers

