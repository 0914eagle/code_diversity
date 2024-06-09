
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
        # Check if the current offer can be accepted
        if num_colors < 3 and num_sections < 10000:
            # Accept the offer and update the variables
            accepted_offers.append(offer)
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1
        else:
            # If the current offer cannot be accepted, break the loop
            break

    # Check if all sections of the fence have been painted
    if num_sections == 10000:
        # If all sections have been painted, return the number of accepted offers
        return len(accepted_offers)
    else:
        # If not all sections have been painted, return "IMPOSSIBLE"
        return "IMPOSSIBLE"

