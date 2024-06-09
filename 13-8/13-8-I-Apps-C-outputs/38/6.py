
def solve(offers):
    # Sort the offers by the first section of the fence
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize the accepted offers
    accepted_offers = []

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # Check if the current offer can be accepted
        if num_sections + (offer[2] - offer[1] + 1) <= 10000 and num_colors < 4:
            # Accept the current offer
            accepted_offers.append(offer)

            # Update the number of sections and colors
            num_sections += (offer[2] - offer[1] + 1)
            num_colors += 1

    # Check if all sections of the fence are painted
    if num_sections == 10000:
        return len(accepted_offers)
    else:
        return "IMPOSSIBLE"

