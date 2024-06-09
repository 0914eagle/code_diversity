
def vanish_monsters(N, A, B, healths):
    # Initialize the number of explosions needed to vanish all monsters
    explosions_needed = 0

    # Sort the healths of the monsters in descending order
    healths.sort(reverse=True)

    # Loop through the monsters and cause explosions until all monsters are vanished
    while sum(healths) > 0:
        # Find the index of the monster with the highest health
        highest_index = healths.index(max(healths))

        # Cause an explosion centered at the monster with the highest health
        healths[highest_index] -= A
        for i in range(len(healths)):
            if i != highest_index:
                healths[i] -= B

        # Increment the number of explosions needed
        explosions_needed += 1

    # Return the number of explosions needed to vanish all monsters
    return explosions_needed

