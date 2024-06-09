
def solve(offers):
    # Sort the offers by the first section of the fence
    sorted_offers = sorted(offers, key=lambda x: x[1])

    # Initialize the variables to keep track of the current color and section
    current_color = ""
    current_section = 0

    # Initialize the count of offers accepted
    count = 0

    # Loop through the sorted offers
    for offer in sorted_offers:
        # If the current color is different from the color in the offer, we need to accept the offer
        if current_color != offer[0]:
            count += 1
            current_color = offer[0]

        # Update the current section to be the last section of the offer
        current_section = offer[2]

    # If the current section is not equal to the total number of sections, we cannot satisfy the requirement of painting all sections
    if current_section != 10000:
        return "IMPOSSIBLE"

    # Return the count of offers accepted
    return count

