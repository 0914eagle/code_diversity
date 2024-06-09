
def solve(offers):
    # Sort the offers by the first section of the fence
    offers.sort(key=lambda x: x[1])

    # Initialize the variables
    current_color = offers[0][0]
    current_section = offers[0][1]
    num_colors = 1
    num_sections = offers[0][2] - offers[0][1] + 1
    accepted_offers = 1

    # Iterate through the remaining offers
    for i in range(1, len(offers)):
        # If the current color is the same as the previous offer, update the current section and number of sections
        if offers[i][0] == current_color:
            current_section = offers[i][2]
            num_sections += offers[i][2] - offers[i][1] + 1
        # If the current color is different from the previous offer, update the number of colors and the current color
        else:
            num_colors += 1
            current_color = offers[i][0]
            current_section = offers[i][1]
            accepted_offers += 1

        # If the number of colors is greater than 3, return "IMPOSSIBLE"
        if num_colors > 3:
            return "IMPOSSIBLE"

    # If all sections are painted and the number of colors is less than or equal to 3, return the number of accepted offers
    if num_sections == 10000 and num_colors <= 3:
        return accepted_offers

    # Otherwise, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

