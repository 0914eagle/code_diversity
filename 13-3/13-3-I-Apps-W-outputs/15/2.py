
def solve(N, A, B, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    # Initialize the number of explosions needed to 0
    explosions_needed = 0
    # Loop through the healths and cause explosions until all monsters are vanished
    for health in healths:
        # If the current health is greater than or equal to A, cause an explosion with center at the current health
        if health >= A:
            explosions_needed += 1
        # If the current health is less than A but greater than or equal to B, cause an explosion with center at the current health - B
        elif health >= B:
            explosions_needed += 1
            health -= B
        # If the current health is less than B, do not cause an explosion and move on to the next health
        else:
            continue
        # If all monsters are vanished, break out of the loop
        if sum(healths) == 0:
            break
    # Return the number of explosions needed to vanish all monsters
    return explosions_needed
