
def solve(snukes, snacks):
    # Initialize a set to store the victims
    victims = set()

    # Iterate over each snack and its corresponding snukes
    for snack, snukes in enumerate(snacks, start=1):
        # If the snukes have the current snack, add them to the victims set
        victims |= set(snukes)

    # Return the number of victims
    return len(victims)

