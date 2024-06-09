
def solve(N, A, B, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    # Initialize the number of explosions needed to 0
    explosions_needed = 0
    # Loop through the healths and cause explosions until all monsters are vanished
    for health in healths:
        # If the current health is less than or equal to 0, skip it
        if health <= 0:
            continue
        # Increment the number of explosions needed
        explosions_needed += 1
        # Subtract B from the current health to damage the monster
        health -= B
        # If the current health is less than or equal to 0, vanish the monster
        if health <= 0:
            continue
        # Subtract A from the current health to damage the surrounding monsters
        for i in range(N):
            if healths[i] > 0:
                healths[i] -= A
    # Return the number of explosions needed
    return explosions_needed

