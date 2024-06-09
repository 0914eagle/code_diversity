
def solve(snakes, snacks):
    # Initialize a set to store the victims
    victims = set()

    # Iterate over each snake
    for snake in snakes:
        # Check if the snake has any snacks
        if not snacks[snake - 1]:
            # If not, add it to the victims set
            victims.add(snake)

    # Return the number of victims
    return len(victims)

