
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])

    # Initialize the variables
    num_colors = 0
    curr_color = ""
    curr_section = 0
    accepted_offers = 0

    # Iterate through the offers
    for offer in offers:
        # Check if the current color is the same as the previous color
        if offer[0] == curr_color:
            # If it is the same, continue painting with the current color
            curr_section = offer[2]
        else:
            # If it is not the same, check if we have reached the maximum number of colors
            if num_colors == 3:
                # If we have, return "IMPOSSIBLE"
                return "IMPOSSIBLE"
            else:
                # If we have not, start painting with a new color
                num_colors += 1
                curr_color = offer[0]
                curr_section = offer[2]

        # Accept the offer
        accepted_offers += 1

    # Return the number of accepted offers
    return accepted_offers

