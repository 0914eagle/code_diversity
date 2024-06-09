
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])
    
    # Initialize the variables to keep track of the colors and sections
    colors = set()
    sections = set()
    
    # Loop through the offers and accept them if they are valid
    for offer in offers:
        color, start, end = offer
        if start not in sections and end not in sections and len(colors) < 3:
            colors.add(color)
            sections.update(range(start, end + 1))
    
    # If all sections of the fence are painted, return the number of accepted offers
    if len(sections) == 10000:
        return len(offers)
    else:
        return "IMPOSSIBLE"

