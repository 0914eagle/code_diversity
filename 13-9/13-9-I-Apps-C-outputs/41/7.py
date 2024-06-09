
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])

    # Initialize the variables
    colors = set()
    sections = set()
    accepted_offers = 0

    # Iterate through the offers
    for offer in offers:
        # Check if the offer is valid
        if offer[1] in sections or offer[2] in sections:
            continue

        # Add the color and sections to the set
        colors.add(offer[0])
        sections.update(range(offer[1], offer[2] + 1))

        # Check if we have accepted all the sections
        if len(sections) == 10000:
            break

        # Increment the number of accepted offers
        accepted_offers += 1

        # Check if we have used more than 3 colors
        if len(colors) > 3:
            return "IMPOSSIBLE"

    # Check if we have accepted all the sections
    if len(sections) == 10000:
        return accepted_offers

    # If we have not accepted all the sections, return IMPOSSIBLE
    return "IMPOSSIBLE"

