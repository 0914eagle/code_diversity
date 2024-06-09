
def solve(offers):
    # Sort the offers by the first section number
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections
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
            # Add the current offer to the result list
            result.append(offer)

            # Increment the number of colors and sections
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1

            # Check if the current offer meets the requirements
            if num_colors <= 3 and num_sections == 10000:
                return result

    # If we reach this point, it means that we could not find a set of offers that meet the requirements
    return "IMPOSSIBLE"

