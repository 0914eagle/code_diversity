
def solve(N, A, B, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    # Initialize the number of explosions needed to 0
    explosions_needed = 0
    # Loop through the healths and cause explosions until all monsters are vanished
    for health in healths:
        # If the health is greater than or equal to A, cause an explosion with center at the current monster
        if health >= A:
            explosions_needed += 1
        # If the health is less than A but greater than or equal to B, cause an explosion with center at the current monster and reduce the health by B
        elif health >= B:
            explosions_needed += 1
            health -= B
        # If the health is less than B, the monster is vanished and we don't need to cause an explosion
        else:
            continue
    return explosions_needed

