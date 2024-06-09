
def solve(offers):
    # Sort the offers by the first section of each offer
    offers.sort(key=lambda x: x[1])
    
    # Initialize the variables to keep track of the number of colors and sections
    num_colors = 0
    num_sections = 0
    
    # Loop through the offers and accept them if they do not violate the constraints
    for offer in offers:
        if num_colors < 3 and num_sections < 10000:
            num_colors += 1
            num_sections += offer[2] - offer[1] + 1
        else:
            break
    
    # If all the sections have been painted and no more than 3 colors are used, return the number of accepted offers
    if num_sections == 10000 and num_colors <= 3:
        return len(offers[:num_sections])
    else:
        return "IMPOSSIBLE"

