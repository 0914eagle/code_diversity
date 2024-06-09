
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize the result list to store the accepted offers
    result = []

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # Check if the current offer overlaps with any of the previously accepted offers
        overlap = False
        for accepted_offer in result:
            if offer[1] <= accepted_offer[2] and offer[2] >= accepted_offer[1]:
                overlap = True
                break

        # If the current offer does not overlap with any of the previously accepted offers, accept it
        if not overlap:
            # Update the number of colors and sections painted
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1

            # Add the current offer to the result list
            result.append(offer)

        # If the current offer overlaps with any of the previously accepted offers, skip it
        else:
            continue

        # If the number of colors exceeds 3, return "IMPOSSIBLE"
        if num_colors > 3:
            return "IMPOSSIBLE"

    # If all the sections of the fence are painted, return the number of accepted offers
    if num_sections == 10000:
        return len(result)

    # If not all the sections of the fence are painted, return "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"

