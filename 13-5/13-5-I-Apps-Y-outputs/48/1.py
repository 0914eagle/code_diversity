
def solve(snukes, snacks):
    # Initialize a set to store the victims
    victims = set()

    # Iterate over each snack and its associated snukes
    for snack, snukes in enumerate(snacks, start=1):
        # Check if any snukes have this snack
        if snukes:
            # Add the snukes with this snack to the victims set
            victims |= set(snukes)

    # Return the number of victims
    return len(victims)

