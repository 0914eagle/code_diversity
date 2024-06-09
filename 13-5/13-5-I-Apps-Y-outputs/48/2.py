
def solve(snakes, snacks):
    # Initialize a set to store the snakes with no snacks
    no_snacks = set()

    # Iterate over the snakes and their snacks
    for snake, snack_list in zip(snakes, snacks):
        # If the snake has no snacks, add it to the set
        if not snack_list:
            no_snacks.add(snake)

    # Return the number of snakes with no snacks
    return len(no_snacks)

