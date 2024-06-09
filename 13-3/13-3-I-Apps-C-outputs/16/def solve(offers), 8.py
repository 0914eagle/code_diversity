
def solve(offers):
    # Sort the offers by the first section of the fence
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the colors and sections
    colors = set()
    sections = set()

    # Loop through the sorted offers and accept them if they can be added to the solution
    for offer in sorted_offers:
        color, start, end = offer
        if color not in colors and len(colors) < 3 and start not in sections and end not in sections:
            colors.add(color)
            sections.update(range(start, end + 1))

    # If all sections of the fence have been painted, return the number of accepted offers
    if len(sections) == 10000:
        return len(offers)
    else:
        return "IMPOSSIBLE"

