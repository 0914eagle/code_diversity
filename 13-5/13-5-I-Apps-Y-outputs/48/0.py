
def solve(snakes, snacks):
    # Initialize a set to store the indices of snakes with no snacks
    no_snacks = set()

    # Iterate over the snakes and their snacks
    for snake, snack in snakes:
        # If the snake has no snacks, add its index to the set
        if snack == 0:
            no_snacks.add(snake)

    # Return the number of snakes with no snacks
    return len(no_snacks)

