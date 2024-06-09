
def paint_fence(offers):
    # Sort the offers by the first section of the fence
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize a list to store the accepted offers
    accepted_offers = []

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # Check if the current offer can be accepted
        if offer[1] == num_sections + 1 and offer[2] <= 10000:
            # Accept the offer and update the number of colors and sections painted
            accepted_offers.append(offer)
            num_colors += 1
            num_sections = offer[2]

        # Check if the current offer cannot be accepted and the fence is already painted with 3 colors
        elif num_colors == 3:
            # Return "IMPOSSIBLE" as the output
            return "IMPOSSIBLE"

    # Check if all sections of the fence are painted
    if num_sections == 10000:
        # Return the number of accepted offers as the output
        return len(accepted_offers)
    else:
        # Return "IMPOSSIBLE" as the output
        return "IMPOSSIBLE"

