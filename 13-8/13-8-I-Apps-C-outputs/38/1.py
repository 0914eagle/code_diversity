
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])
    
    # Initialize the variables to keep track of the colors and sections
    colors = set()
    sections = set()
    
    # Iterate through the offers and accept them if they are valid
    for offer in offers:
        color, first_section, last_section = offer
        if color not in colors and first_section not in sections and last_section not in sections:
            colors.add(color)
            sections.update(range(first_section, last_section + 1))
    
    # If all sections are painted, return the number of accepted offers
    if len(sections) == 10000:
        return len(offers)
    else:
        return "IMPOSSIBLE"

