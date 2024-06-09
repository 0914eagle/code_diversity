
def solve(N, K, health):
    # Initialize variables
    attacks = 0
    special_moves = K
    health = sorted(health, reverse=True)

    # Loop through the monsters
    for i in range(N):
        # If the monster's health is 1, we can win without using Special Move
        if health[i] == 1:
            return attacks

        # If we have Special Move available, use it
        if special_moves > 0:
            special_moves -= 1
            health[i] = 0
            continue

        # Do Attack
        attacks += 1
        health[i] -= 1

    # If we reach this point, we need to do Attack at least once more
    return attacks + 1

