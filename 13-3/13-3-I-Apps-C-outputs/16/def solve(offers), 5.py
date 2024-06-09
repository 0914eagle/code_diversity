
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])
    
    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0
    
    # Initialize a set to store the colors that have been used
    colors = set()
    
    # Iterate through the offers
    for offer in offers:
        # Check if the offer can be accepted
        if offer[1] == num_sections + 1 and len(colors) < 3:
            # Accept the offer and update the variables
            num_colors += 1
            num_sections = offer[2]
            colors.add(offer[0])
        else:
            # The offer cannot be accepted, so break the loop
            break
    
    # Check if all sections of the fence have been painted
    if num_sections == 10000:
        # Return the number of offers accepted
        return len(offers[:num_sections])
    else:
        # Return "IMPOSSIBLE" if not all sections have been painted
        return "IMPOSSIBLE"

