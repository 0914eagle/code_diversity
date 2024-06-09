
def solve(offers):
    # Sort the offers by the first section of the fence
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize the list to store the accepted offers
    accepted_offers = []

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # Check if the current offer overlaps with the previous offer
        if num_sections > 0 and offer[1] <= accepted_offers[-1][2]:
            # If it overlaps, merge the offers and update the variables
            accepted_offers[-1][2] = max(accepted_offers[-1][2], offer[2])
            num_sections += offer[2] - accepted_offers[-1][1] + 1
        else:
            # If it does not overlap, add the offer to the list of accepted offers
            accepted_offers.append(offer)
            num_sections += offer[2] - offer[1] + 1
            num_colors += 1

        # Check if the maximum number of colors has been reached
        if num_colors > 3:
            return "IMPOSSIBLE"

    # Check if all sections have been painted
    if num_sections == 10000:
        return len(accepted_offers)
    else:
        return "IMPOSSIBLE"

