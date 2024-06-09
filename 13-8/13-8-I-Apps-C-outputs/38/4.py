
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])

    # Initialize the variables to keep track of the colors and sections
    colors = set()
    sections = set()

    # Loop through the offers and add them to the list of colors and sections
    for offer in offers:
        colors.add(offer[0])
        sections.update(range(offer[1], offer[2] + 1))

    # If all sections are painted and there are at most 3 colors, return the number of offers accepted
    if len(sections) == 10000 and len(colors) <= 3:
        return len(offers)

    # Otherwise, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

