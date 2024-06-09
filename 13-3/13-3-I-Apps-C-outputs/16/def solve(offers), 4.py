
def solve(offers):
    # Sort the offers by the first section of each offer
    offers.sort(key=lambda x: x[1])
    
    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0
    
    # Initialize a list to store the colors that have been used
    colors = []
    
    # Iterate through the offers and accept them if they can be accepted
    for offer in offers:
        # Check if the offer can be accepted
        if offer[1] == num_sections + 1 and offer[2] <= 10000:
            # Accept the offer and update the variables
            num_colors += 1
            num_sections = offer[2]
            colors.append(offer[0])
        else:
            # The offer cannot be accepted, break the loop
            break
    
    # Check if all sections have been painted
    if num_sections == 10000:
        # All sections have been painted, return the number of offers accepted
        return len(colors)
    else:
        # Not all sections have been painted, return "IMPOSSIBLE"
        return "IMPOSSIBLE"

