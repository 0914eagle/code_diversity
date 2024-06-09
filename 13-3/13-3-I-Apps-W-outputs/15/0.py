
def vanish_monsters(N, A, B, healths):
    # Sort the healths in descending order
    healths.sort(reverse=True)
    # Initialize the number of explosions needed to vanish all monsters
    explosions_needed = 0
    # Loop through the healths and cause explosions until all monsters are vanished
    for i in range(N):
        # Calculate the current health of the monster
        current_health = healths[i]
        # Check if the monster is already vanished
        if current_health == 0:
            continue
        # Calculate the damage caused by the explosion
        damage = A - B * (N - i - 1)
        # Update the current health of the monster
        healths[i] -= damage
        # Check if the monster has vanished
        if healths[i] <= 0:
            explosions_needed += 1
    return explosions_needed

