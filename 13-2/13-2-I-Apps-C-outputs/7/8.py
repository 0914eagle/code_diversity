
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize the list to store the accepted offers
    accepted_offers = []

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # Check if the current offer overlaps with any of the accepted offers
        overlap = False
        for accepted_offer in accepted_offers:
            if offer[1] <= accepted_offer[2] and offer[2] >= accepted_offer[1]:
                overlap = True
                break

        # If the current offer does not overlap with any of the accepted offers, accept it
        if not overlap:
            accepted_offers.append(offer)
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1

        # If the current offer overlaps with any of the accepted offers, reject it
        else:
            continue

        # If the number of colors exceeds 3, reject the current offer
        if num_colors > 3:
            accepted_offers.pop()
            num_colors -= 1
            num_sections -= offer[2] - offer[1] + 1

    # If all the sections of the fence are painted, return the number of accepted offers
    if num_sections == 10000:
        return len(accepted_offers)

    # If not all the sections of the fence are painted, return "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"

