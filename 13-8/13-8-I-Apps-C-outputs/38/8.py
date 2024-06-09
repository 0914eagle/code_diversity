
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])
    
    # Initialize the variables to keep track of the number of colors and sections painted
    num_colors = 0
    num_sections = 0
    
    # Iterate through the offers and accept them if they can be added to the solution
    for offer in offers:
        # Check if the offer can be added to the solution
        if offer[1] == num_sections + 1 and offer[2] <= num_sections + 10000:
            # Add the offer to the solution
            num_sections += offer[2] - offer[1] + 1
            num_colors += 1
            # Check if the solution is complete
            if num_sections == 10000:
                break
        # If the offer cannot be added to the solution, return "IMPOSSIBLE"
        else:
            return "IMPOSSIBLE"
    
    # If the solution is complete, return the number of offers accepted
    if num_sections == 10000:
        return num_colors
    # If the solution is not complete, return "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"

