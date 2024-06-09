
def solve(offers):
    # Sort the offers by the first section of the fence
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0

    # Initialize the result list to store the accepted offers
    result = []

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # Check if the current offer overlaps with the previous offer
        if num_sections > 0 and offer[1] <= result[-1][2]:
            # If it overlaps, merge the offers and update the number of colors and sections painted
            result[-1][2] = max(result[-1][2], offer[2])
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1
        else:
            # If it doesn't overlap, add the offer to the result list and update the number of colors and sections painted
            result.append(offer)
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1

        # Check if the current offer exceeds the maximum number of colors allowed
        if num_colors > 3:
            return "IMPOSSIBLE"

    # Check if all sections of the fence have been painted
    if num_sections == 10000:
        return len(result)
    else:
        return "IMPOSSIBLE"

