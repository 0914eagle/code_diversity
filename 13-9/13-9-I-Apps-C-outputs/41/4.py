
def solve(offers):
    # Sort the offers by the first section of each offer
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the colors and sections
    colors = set()
    sections = set()
    accepted_offers = 0

    # Iterate through the sorted offers
    for offer in sorted_offers:
        # If the color of the current offer is not in the colors set, add it to the colors set
        if offer[0] not in colors:
            colors.add(offer[0])

        # If the current offer intersects with any of the previous offers, skip it
        if any(offer[1] <= section <= offer[2] for section in sections):
            continue

        # Add the current offer to the accepted offers
        accepted_offers += 1

        # Add the sections of the current offer to the sections set
        sections.update(range(offer[1], offer[2] + 1))

        # If the number of colors exceeds 3, return "IMPOSSIBLE"
        if len(colors) > 3:
            return "IMPOSSIBLE"

    # If all the sections have been painted, return the number of accepted offers
    if len(sections) == 10000:
        return accepted_offers

    # If not all the sections have been painted, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

